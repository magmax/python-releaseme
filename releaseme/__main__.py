import argparse
from .actions import Actions


def main():
    actions = Actions()

    parser = argparse.ArgumentParser(description='Manage project versions')
    parser.add_argument('command', nargs='?', default='increment',
                        choices=actions.choices,
                        help='Action to be performed')
    parser.add_argument('--file',
                        nargs='*',
                        help='File that manages the version')
    parser.add_argument('--git',
                        action="store_true", default=False,
                        help='Manages versions with Git tags')

    args = parser.parse_args()

    new_version = getattr(actions, args.command)(args)

    print("New version: %s" % new_version)


if __name__ == '__main__':
    main()
