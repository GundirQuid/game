import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_ascii_letters(self):
        self.assertTrue("Hello World".isascii())
        self.assertFalse("Hello Worldñn►╬║".isascii())

    def test_digits(self):
        self.assertTrue('1234567890'.isdigit())
        self.assertFalse('123456789O'.isdigit())

    def test_capitalize(self):
        self.assertEqual(''.capitalize(), '')
        self.assertEqual('hello world'.capitalize(), 'Hello world')

    def test_casefold(self):
        self.assertEqual('ß'.casefold(), 'ss')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            _ = s.split(2)
