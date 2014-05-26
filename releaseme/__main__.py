import os
import argparse
from .actions import Actions
from pluginloader import PluginLoader


def main():
    plugin_path = os.path.join(
        os.path.dirname(__file__),
        'plugins',
        )
    plugin_mgr = PluginLoader()
    plugin_mgr.load_directory(plugin_path)

    plugins = [c() for n,c in plugin_mgr.plugins.items()]

    actions = Actions(plugins)

    parser = argparse.ArgumentParser(description='Manage project versions')
    parser.add_argument('command', nargs='?', default='increment',
                        choices=actions.choices,
                        help='Action to be performed')


    for clazz in plugins:
        group = parser.add_argument_group(clazz.name, clazz.description)
        clazz.options(group)

    args = parser.parse_args()

    new_version = getattr(actions, args.command)(args)

    print("New version: %s" % new_version)


if __name__ == '__main__':
    main()
