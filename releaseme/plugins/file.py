from releaseme.version import Version


class File(object):
    name = 'File'
    description = 'Manages versions on files'

    @staticmethod
    def options(group):
        group.add_argument('--file',
                           nargs='*',
                           help='File that manages the version')

    def initialize(self, args):
        self.files = args.file

    def get_version(self):
        return max(Version(self._read(x))
                   for x in self.files)

    def _read(self, filename):
        with open(filename) as fd:
            return fd.read().decode('utf-8')

    def set_version(self):
        pass
