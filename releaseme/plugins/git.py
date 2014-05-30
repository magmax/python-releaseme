from releaseme.version import Version
from releaseme import sh


class Git(object):
    name = 'Git'
    description = 'Git repository management'

    @staticmethod
    def options(group):
        group.add_argument('--git',
                           action="store_true", default=False,
                           help='Manages versions with Git tags')

    def initialize(self, args):
        pass

    def get_version(self):
        stdout, stderr, rc = sh.run('git', 'tag')
        return max(Version(tag)
                   for tag in (stdout or '').split('\n'))

    def set_version(self):
        pass
