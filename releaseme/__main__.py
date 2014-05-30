import os
import logging
import argparse
from .actions import Actions
from pluginloader import PluginLoader


logger = logging.getLogger('releaseme')


def logging_settings(args):
    verbosity = min(2, args.verbose)
    level = [logging.WARNING, logging.INFO, logging.DEBUG][verbosity]
    logging.basicConfig(
        level=level,
#        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        format='%(msecs)0.2f %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M',
        )


def check_plugin(name, clazz):
    methods = ('options', 'initialize', 'get_version', 'set_version')
    return all(hasattr(clazz, m) for m in methods)


def main():
    plugin_path = os.path.join(
        os.path.dirname(__file__),
        'plugins',
        )
    plugin_mgr = PluginLoader()
    plugin_mgr.load_directory(plugin_path, onlyif=check_plugin)

    plugins = [c() for n, c in plugin_mgr.plugins.items()]

    actions = Actions(plugins)

    parser = argparse.ArgumentParser(description='Manage project versions')
    parser.add_argument('command', nargs='?', default='increment',
                        choices=actions.choices,
                        help='Action to be performed')
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help='Verbosity level')

    for plugin in plugins:
        group = parser.add_argument_group(plugin.name, plugin.description)
        plugin.options(group)

    args = parser.parse_args()
    logging_settings(args)

    # initialize plugins
    for plugin in plugins:
        plugin.initialize(args)

    # retrieve the new version
    new_version = None
    for plugin in plugins:
        logger.debug('Getting version from plugin %s', plugin.name)
        new_version = max(new_version, plugin.get_version())
        logger.debug('Current version: %s', new_version)
    if args.command == 'increment':
        pass

    print("New version: %s" % new_version)


if __name__ == '__main__':
    main()
