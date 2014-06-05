from releaseme.version import Version
from releaseme import sh
from releaseme import errors


class Git(object):
    name = 'Git'
    description = 'Git repository management'
    should_run = True
    pre_increment = True
    post_increment = False

    @staticmethod
    def options(group):
        group.add_argument('--git',
                           action="store_true", default=False,
                           help='Manages versions with Git tags')

    def initialize(self, args):
        self.should_run = args.git

    def get_version(self):
        if not self.should_run:
            return Version('0')

        stdout, stderr, rc = sh.run('git', 'tag')
        return max(Version(tag)
                   for tag in (stdout or '').split('\n'))

    def set_version(self, version):
        if not self.should_run:
            return

        stdout, stderr, rc = sh.run('git', 'tag', str(version))
        if rc != 0:
            raise errors.PluginError('Repository could not be tagged')
