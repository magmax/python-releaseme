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

    args = parser.parse_args()

    getattr(actions, args.command)(args)


if __name__ == '__main__':
    main()
