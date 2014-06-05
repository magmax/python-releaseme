import os
import tempfile
import unittest
import pexpect

from .base import FileAcceptanceTest


class FileWithContent(FileAcceptanceTest, unittest.TestCase):
    def test_one_line_file_is_maintained(self):
        filename = self.versions_file('__version__ = "0.1.2"')

        sut = pexpect.spawn('python -m releaseme increment --file=%s -v'
                            % filename)

        sut.expect('0.1.3', timeout=2)
        sut.wait()
        self.assertFileContent(filename, '__version__ = "0.1.3"')

    def test_several_lines_file_is_maintained(self):
        filename = self.versions_file(
            'foo = "bar"\n__version__ = "0.1.2"\nfoo = "bar"')

        sut = pexpect.spawn('python -m releaseme increment --file=%s -v'
                            % filename)

        sut.expect('0.1.3', timeout=2)
        sut.wait()
        self.assertFileContent(
            filename,
            'foo = "bar"\n__version__ = "0.1.3"\nfoo = "bar"')
