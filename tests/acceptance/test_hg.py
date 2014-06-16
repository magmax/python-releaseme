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

        sut.expect('0', timeout=2)
        self.assertEqual(2, sut.wait())

    def test_previously_tagged(self):
        self.add_commit()
        self.add_tag('1.2.3')
        sut = pexpect.spawn('python -m releaseme increment --hg -v',
                            cwd=self.cwd)

        self.assertEqual(0, sut.wait())

        self.assertTag('1.2.3')
