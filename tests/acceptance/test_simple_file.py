import os
import tempfile
import unittest
import pexpect

from .base import AcceptanceTest


class SimpleVersionFile(AcceptanceTest, unittest.TestCase):
    def test_increment_the_file_content(self):
        filename = self.versions_file('0.1.2')

        sut = pexpect.spawn('python -m releaseme increment --file=%s'
                            % filename)

        sut.expect('0.1.3', timeout=2)
        self.assertFileContent(filename, '0.1.3')

    def test_increment_the_file_content_again(self):
        filename = self.versions_file('1.2.3')

        sut = pexpect.spawn('python -m releaseme increment --file=%s'
                            % filename)

        sut.expect('1.2.4', timeout=2)
        self.assertFileContent(filename, '1.2.4')

    def test_rare_case(self):
        filename = self.versions_file('0.1.1')

        sut = pexpect.spawn('python -m releaseme increment --file=%s'
                            % filename)

        sut.expect('0.1.2', timeout=2)
        self.assertFileContent(filename, '0.1.2')
