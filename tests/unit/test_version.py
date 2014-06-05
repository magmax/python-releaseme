import unittest

from releaseme.version import Version


class VersionTest(unittest.TestCase):
    def test_to_string(self):
        sut = Version('0.0.0')

        self.assertEquals('0.0.0', str(sut))
        self.assertEquals('0.0.0', sut.content)

    def test_empty_string(self):
        sut = Version('')

        self.assertEquals('0', str(sut))
        self.assertEquals('', sut.content)

    def test_to_string_with_strings(self):
        sut = Version('0.0.0-example1')

        self.assertEquals('0.0.0-example1', sut.content)

    def test_bug_1_with_enters(self):
        sut = Version('0.1.1\r\n')

        self.assertEquals('0.1.1\r\n', sut.content)
        self.assertEquals('0.1.1', str(sut))


class VersionIncrementTest(unittest.TestCase):
    def test_basic_increment(self):
        sut = Version('0.0.0')

        sut.increment()

        self.assertEquals('0.0.1', sut.content)

    def test_basic_increment_again(self):
        sut = Version('0.0.0')

        sut.increment()
        sut.increment()

        self.assertEquals('0.0.2', sut.content)

    def test_increment_with_string(self):
        sut = Version('0.0.0-example1')

        sut.increment()

        self.assertEquals('0.0.1-example1', sut.content)

    def test_operator_with_number(self):
        sut = Version('0.0.0')

        sut += 1

        self.assertEquals('0.0.1', sut.content)
        self.assertIsInstance(sut, Version)


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


class ContainingTextTest(unittest.TestCase):
    def test_basic_python_version(self):
        initial = '__version__ = "0.1"'
        expected = initial
        sut = Version(initial)

        self.assertEqual(expected, sut.content)

    def test_basic_python_version_increment(self):
        initial = '__version__ = "0.1"'
        expected = '__version__ = "0.2"'
        sut = Version(initial)

        sut += 1

        self.assertEqual(expected, sut.content)
