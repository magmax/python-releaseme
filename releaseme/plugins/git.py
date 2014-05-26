class Git(object):
    name = 'Git'
    description = 'Git repository management'

    @staticmethod
    def options(group):
        group.add_argument('--git',
                           action="store_true", default=False,
                           help='Manages versions with Git tags')

    def get_version(self):
        pass

    def set_version(self):
        pass
