class File(object):
    name = 'File'
    description = 'Manages versions on files'

    @staticmethod
    def options(group):
        group.add_argument('--file',
                           nargs='*',
                           help='File that manages the version')

    def get_version(self):
        pass

    def set_version(self):
        pass
