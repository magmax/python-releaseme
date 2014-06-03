import os
import shutil
import tempfile
import subprocess
import pexpect


class FileAcceptanceTest(object):
    def setUp(self):
        self._tempfiles = []

    def tearDown(self):
        for tmp in self._tempfiles:
            os.remove(tmp)

    def versions_file(self, version):
        with tempfile.NamedTemporaryFile(delete=False) as fd:
            fd.write(version)
            fd.flush()
            self._tempfiles.append(fd.name)
            return fd.name

    def assertFileContent(self, filename, version):
        with file(filename) as fd:
            self.assertEquals(version, fd.read())


class GitAcceptanceTest(object):
    def setUp(self):
        self._git = tempfile.mkdtemp()
        subprocess.check_call('git init'.split(),
                              cwd=self._git,
                              stdout=subprocess.PIPE
                              )

    def tearDown(self):
        shutil.rmtree(self._git)

    @property
    def cwd(self):
        return self._git

    def add_commit(self):
        with open(os.path.join(self._git, 'foo')) as fd:
            fd.write('foo\n')
        subprocess.check_call('git add foo'.split(),
                              cwd=self._git)
        subprocess.check_call('git commit -m "foo"'.split(),
                              cwd=self._git)

    def assertTag(self, tag):
        if subprocess.check_call(['git', 'tag', tag],
                                 cwd=self._git) == 0:
            self.fail('Tag %s does not exist' % tag)
