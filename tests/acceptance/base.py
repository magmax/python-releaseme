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
        self.shell('git init')

    def tearDown(self):
        shutil.rmtree(self._git)

    @property
    def cwd(self):
        return self._git

    def add_commit(self):
        filename = 'foo'
        with open(os.path.join(self._git, filename), 'w+') as fd:
            fd.write('foo\n')
        self.shell('git add %s' % filename)
        self.shell('git commit -m "%s"' % filename)

    def add_tag(self, tag):
        self.shell('git tag "%s"' % tag.strip())

    def assertTag(self, tag):
        tags, stderr, rc = self.shell('git tag')
        stdout, stderr, rc = self.shell('git tag "%s"')
        self.assertEqual(2, rc, 'Tag %s does not exist. Tag list:\n %s'
                         % (tag, tags))

    def shell(self, cmd):
        p = subprocess.Popen(cmd.split(),
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             cwd=self._git,
                             )
        stdout, stderr = p.communicate()
        rc = p.wait()

        return stdout, stderr, rc
