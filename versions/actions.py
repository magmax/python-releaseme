from .version import Version


class Actions(object):
    def increment(self, options):
        for filename in options.file:
            with file(filename) as fd:
                version = Version(fd.read())

            version = Version('0.1.3')
            with file(filename, 'w') as fd:
                fd.write(str(version))
            print version

    def get(self):
        pass

    @property
    def choices(self):
        return ['increment', 'get']
        return [x
                for x in self.__dict__.keys()
                if x is not 'choices' and not x.startswith('_')]
