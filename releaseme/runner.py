import os
import logging
import argparse
from pluginloader import PluginLoader
from .version import Version
from . import errors

logger = logging.getLogger('releaseme')


def logging_settings(args):
    verbosity = min(2, args.verbose)
    level = [logging.WARNING, logging.INFO, logging.DEBUG][verbosity]
    logging.basicConfig(
        level=level,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M',
        )
    logger.setLevel(level)


class Runner(object):
    def __init__(self):
        self.plugins = None
        self.args = None

    def run(self):
        try:
            self._load_plugins()
            self._parse_args()
            self._initialize()
            version = self._retrieve_version()
            if self.args.command == 'get':
                print("Current version: %s" % version)
                return

            if self.args.command == 'increment':
                logger.info("Previous version: %s" % version)
                self._set_pre_incr_version(version)
                version += 1

                logger.info("Increasing version to: %s" % version)
                self._set_post_incr_version(version)
        except errors.PluginError as e:
            print(str(e))
            return 2

    def _load_plugins(self):
        plugin_path = os.path.join(
            os.path.dirname(__file__),
            'plugins',
            )
        plugin_mgr = PluginLoader()
        plugin_mgr.load_directory(plugin_path, onlyif=self._check_plugin)

        self.plugins = [c() for n, c in plugin_mgr.plugins.items()]

    def _parse_args(self):
        parser = argparse.ArgumentParser(description='Manage project versions')
        parser.add_argument('command', nargs='?', default='increment',
                            choices=['get', 'increment'],
                            help='Action to be performed')
        parser.add_argument('-v', '--verbose', action='count', default=0,
                            help='Verbosity level')

        for plugin in self.plugins:
            group = parser.add_argument_group(plugin.name, plugin.description)
            plugin.options(group)

        self.args = parser.parse_args()
        logging_settings(self.args)

    def _initialize(self):
        for plugin in self.plugins:
            plugin.initialize(self.args)

    def _retrieve_version(self):
        result = Version('0')
        for plugin in self.plugins:
            logger.debug('Getting version from plugin %s', plugin.name)
            result = max(result, plugin.get_version())
            logger.debug('Current version: %s', result)
        logger.info("Current version: %s" % result)
        return result

    def _set_pre_incr_version(self, version):
        for plugin in self.plugins:
            if plugin.pre_increment:
                plugin.set_version(version)

    def _set_post_incr_version(self, version):
        for plugin in self.plugins:
            if plugin.post_increment:
                plugin.set_version(version)

    def _check_plugin(self, name, clazz):
        methods = ('options', 'initialize', 'get_version', 'set_version')
        return all(hasattr(clazz, m) for m in methods)
