import argparse


class Actions(object):
    def increment(self, options):
        with file(options.file) as fd:
            version = fd.read()

        version = '0.1.3'
        with file(options.file, 'w') as fd:
            fd.write(version)
        print version

    def get(self):
        pass

    @property
    def choices(self):
        return ['increment', 'get']
        return [x
                for x in self.__dict__.keys()
                if x is not 'choices' and not x.startswith('_')]


def main():
    actions = Actions()

    parser = argparse.ArgumentParser(description='Manage project versions')
    parser.add_argument('command', nargs='?', default='increment',
                        choices=actions.choices,
                        help='Action to be performed')
    parser.add_argument('--file',
                        help='File that manages the version')

    args = parser.parse_args()

    getattr(actions, args.command)(args)


if __name__ == '__main__':
    main()
