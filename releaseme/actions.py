# -*- coding: utf-8 -*-
import subprocess
from .version import Version


class Actions(object):
    def increment(self, options):
        version = self._get_higher_version(options)
        version.increment()
        self._set_version(options, version)
        return version

    def _get_higher_version(self, options):
        return max(self._versions(options))

    def _versions(self, options):
        yield Version('0.0.0')
        if options.file:
            for filename in options.file:
                yield self._get_version_from_file(filename)
        if options.git:
            for v in self._get_version_from_git():
                yield v

    def _get_version_from_file(self, filename):
            with open(filename) as fd:
                content = fd.read().decode('utf-8')
                print content
                return Version(content)

    def _get_version_from_git(self):
        stdout, stderr, rc = self._shell('git', 'tag')
        for tag in stdout or []:
            yield Version(tag)

    def _shell(self, *command):
        p = subprocess.Popen(command,
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE)
        stdout, stderr = p.communicate()
        return stdout, stderr, p.wait()

    def _set_version(self, options, version):
        if options.file:
            for filename in options.file:
                self._save_version_to_file(filename, version)
        if options.git:
            self._shell('git', 'tag', str(version))

    def _save_version_to_file(self, filename, version):
        with open(filename, 'wt') as fd:
            fd.write(str(version))

    def get(self, options):
        return self._get_higher_version(options)

    @property
    def choices(self):
        return sorted([x
                       for x in dir(self)
                       if x is not 'choices' and not x.startswith('_')])
