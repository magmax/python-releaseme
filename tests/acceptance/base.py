import os
import shutil
import tempfile
import subprocess
import pexpect


class FileAcceptanceMixin(object):
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


def shell(cmd, cwd):
    p = subprocess.Popen(cmd.split(),
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         cwd=cwd,
                         )
    stdout, stderr = p.communicate()
    rc = p.wait()

    return stdout, stderr, rc


class GitAcceptanceMixin():
    def setUp(self):
        self._git = tempfile.mkdtemp()
        self.shell('git init')

    def tearDown(self):
        shutil.rmtree(self._git)

    @property
    def cwd(self):
        return self._git

    def shell(self, cmd):
        return shell(cmd, cwd=self._git)

    def add_commit(self):
        filename = 'foo'
        with open(os.path.join(self._git, filename), 'a+') as fd:
            fd.write('foo\n')
        self.shell('git add %s' % filename)
        self.shell('git commit -m "%s"' % filename)

    def add_tag(self, tag):
        self.shell('git tag "%s"' % tag.strip())

    def assertTag(self, tag):
        tags, stderr, rc = self.shell('git tag')
        self.assertIn(tag, tags.splitlines(),
                      'Tag %s does not exist. Tag list:\n%s'
                      % (tag, tags))


class HgAcceptanceMixin():
    def setUp(self):
        self._hg = tempfile.mkdtemp()
        self.shell('hg init')

    def tearDown(self):
        shutil.rmtree(self._hg)

    @property
    def cwd(self):
        return self._hg

    def shell(self, cmd):
        return shell(cmd, cwd=self._hg)

    def add_commit(self):
        filename = 'foo'
        with open(os.path.join(self._hg, filename), 'a+') as fd:
            fd.write('foo\n')
        self.shell('hg add %s' % filename)
        self.shell('hg commit -m "%s"' % filename)

    def add_tag(self, tag):
        self.shell('hg tag "%s"' % tag.strip())

    def assertTag(self, tag):
        tags, stderr, rc = self.shell('hg -y tags')
        self.assertIn(tag, [x.split()[0] for x in tags.splitlines()],
                      'Tag %s does not exist. Tag list:\n%s'
                      % (tag, tags))
