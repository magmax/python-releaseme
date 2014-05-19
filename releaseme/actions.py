# -*- coding: utf-8 -*-
from .version import Version


class Actions(object):
    def increment(self, options):
        version = None

        for filename in options.file:
            with open(filename) as fd:
                v = Version(fd.read().decode('utf-8'))
            if version is None or v > version:
                version = v

        version.increment()
        str_version = str(version)

        for filename in options.file:
            with open(filename, 'wt') as fd:
                fd.write(str_version)

        return version

    def get(self):
        pass

    @property
    def choices(self):
        return ['increment', 'get']
        return [x
                for x in self.__dict__.keys()
                if x is not 'choices' and not x.startswith('_')]
