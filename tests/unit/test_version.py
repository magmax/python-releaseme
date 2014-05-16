import unittest

from releaseme.version import Version


class VersionTest(unittest.TestCase):
    def test_to_string(self):
        sut = Version('0.0.0')

        self.assertEquals('0.0.0', str(sut))

    def test_split(self):
        sut = Version('0.0.0')

        self.assertEquals([0, 0, 0], sut.split())

    def test_split_respect_strings(self):
        sut = Version('0.0.0-example1')

        self.assertEquals([0, 0, 0, 'example1'], sut.split())

    def test_to_string_with_strings(self):
        sut = Version('0.0.0-example1')

        self.assertEquals('0.0.0-example1', str(sut))


class VersionIncrementTest(unittest.TestCase):
    def test_basic_increment(self):
        sut = Version('0.0.0')

        sut.increment()

        self.assertEquals('0.0.1', str(sut))

    def test_basic_increment_again(self):
        sut = Version('0.0.0')

        sut.increment()
        sut.increment()

        self.assertEquals('0.0.2', str(sut))

    def test_increment_with_string(self):
        sut = Version('0.0.0-example1')

        sut.increment()

        self.assertEquals('0.0.1-example1', str(sut))
