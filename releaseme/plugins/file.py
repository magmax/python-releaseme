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
        self.files = args.file or []

    def get_version(self):
        if not self.files:
            return Version('0')
        return max(Version(self._read(x))
                   for x in self.files)

    def set_version(self, version):
        for filename in self.files:
            self._save_version_to_file(filename, version)

    def _read(self, filename):
        with open(filename) as fd:
            return fd.read().decode('utf-8')

    def _save_version_to_file(self, filename, version):
        with open(filename, 'wt') as fd:
            fd.write(str(version))
