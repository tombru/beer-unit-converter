import unittest

from conv import l_to_ebc, srm_to_ebc

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_l_to_ebc(self):
        self.assertEqual(l_to_ebc(12), 31)

    def test_srm_to_ebc(self):
        self.assertEqual(srm_to_ebc(14), 28)

if __name__ == '__main__':
    unittest.main()