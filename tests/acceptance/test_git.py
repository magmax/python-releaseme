import os
import tempfile
import unittest
import shutil
import pexpect

from .base import GitAcceptanceTest


class BasicGitTest(GitAcceptanceTest, unittest.TestCase):
    def test_with_no_tags(self):
        sut = pexpect.spawn('python -m releaseme increment --git -v',
                            cwd=self.cwd)

        sut.expect('0', timeout=2)
        self.assertEqual(2, sut.wait())

#        self.assertTag('0')
