import os
import tempfile
import unittest
import shutil
import pexpect

from .base import HgAcceptanceMixin


class BasicHgTest(HgAcceptanceMixin, unittest.TestCase):
    def test_with_no_tags(self):
        self.add_commit()
        sut = pexpect.spawn('python -m releaseme increment --hg -v',
                            cwd=self.cwd)

        sut.expect('0', timeout=5)
        # self.assertEquals(2, sut.wait())   # Fails with some hg versions
        self.assertNotEquals(0, sut.wait())

    def test_previously_tagged(self):
        self.add_commit()
        self.add_tag('1.2.3')
        sut = pexpect.spawn('python -m releaseme increment --hg -v',
                            cwd=self.cwd)

        sut.wait()
        # self.assertEquals(0, sut.wait())  # Fails with some hg versions

        self.assertTag('1.2.3')
