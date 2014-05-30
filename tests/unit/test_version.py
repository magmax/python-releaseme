import unittest

from releaseme.version import Version


class VersionTest(unittest.TestCase):
    def test_to_string(self):
        sut = Version('0.0.0')

        self.assertEquals('0.0.0', str(sut))

    def test_empty_string(self):
        sut = Version('')

        self.assertEquals('0', str(sut))

    def test_split(self):
        sut = Version('0.0.0')

        self.assertEquals([0, 0, 0], sut.split())

    def test_split_respect_strings(self):
        sut = Version('0.0.0-example1')

        self.assertEquals([0, 0, 0, 'example1'], sut.split())

    def test_to_string_with_strings(self):
        sut = Version('0.0.0-example1')

        self.assertEquals('0.0.0-example1', str(sut))

    def test_bug_1_with_enters(self):
        sut = Version('0.1.1\r\n')

        self.assertEquals('0.1.1\r\n', str(sut))


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


class VersionComparisionTest(unittest.TestCase):
    def test_basic_comparision(self):
        a = Version('0')
        b = Version('1')

        self.assertTrue(a < b)
        self.assertTrue(b > a)
        self.assertEqual(b, max(a, b))
        self.assertEqual(b, max(b, a))

    def test_basic_comparision_with_two_numbers(self):
        b = Version('0.2')
        a = Version('0.1')

        self.assertTrue(a < b)
        self.assertTrue(b > a)
        self.assertEqual(b, max(a, b))
        self.assertEqual(b, max(b, a))

    def test_with_strings(self):
        b = Version('0.1-foo2')
        a = Version('0.1-foo1')

        self.assertTrue(a < b)
        self.assertTrue(b > a)
        self.assertEqual(b, max(a, b))
        self.assertEqual(b, max(b, a))
