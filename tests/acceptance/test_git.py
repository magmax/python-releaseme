import os
import tempfile
import unittest
import pexpect

from .base import GitAcceptanceTest


class BasicGitTest(GitAcceptanceTest, unittest.TestCase):
    def test_with_no_tags(self):

        sut = pexpect.spawn('python -m releaseme increment --git')

        sut.expect('0.0.0', timeout=2)

        self.assertTag('0.0.0')
