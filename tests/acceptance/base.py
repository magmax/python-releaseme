import os
import tempfile
import pexpect


class AcceptanceTest(object):
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
