# -*- coding: utf-8 -*-
from .version import Version


class Actions(object):
    def increment(self, options):
        version = None

        for filename in options.file:
            version = max(version,
                          self._get_version_from_file(filename))

        version.increment()

        for filename in options.file:
            self._save_version_to_file(filename, version)

        return version

    def _get_version_from_file(self, filename):
            with open(filename) as fd:
                return Version(fd.read().decode('utf-8'))

    def _save_version_to_file(self, filename, version):
        with open(filename, 'wt') as fd:
            fd.write(str(version))

    def get(self):
        pass

    @property
    def choices(self):
        return sorted([x
                       for x in dir(self)
                       if x is not 'choices' and not x.startswith('_')])
