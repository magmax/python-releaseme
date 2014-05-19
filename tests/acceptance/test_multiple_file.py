import os
import tempfile
import unittest
import pexpect

from .base import FileAcceptanceTest


class MultipleVersionFile(FileAcceptanceTest, unittest.TestCase):
    def test_takes_the_max_in_two_files(self):
        filename1 = self.versions_file('0.1.2')
        filename2 = self.versions_file('0.1.3')

        sut = pexpect.spawn('python -m releaseme increment --file %s %s'
                            % (filename1, filename2))

        sut.expect('0.1.4', timeout=2)
        self.assertFileContent(filename1, '0.1.4')
        self.assertFileContent(filename2, '0.1.4')
