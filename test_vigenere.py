import unittest
import vigenere

class TestVigenere(unittest.TestCase):

    def test_create_keystream(self):
        self.assertEqual(vigenere.key('hello world', 'foo'), 'foofoofoofo')
        self.assertEqual(vigenere.key('foo', 'bar'), 'bar')
        self.assertEqual(vigenere.key('sfx', 'foobar'), 'foo')
        self.assertEqual(vigenere.key('a    b', 'foo'), 'foofoo')

    def test_cifra(self):
        self.assertEqual(vigenere.cifra('hello world', 'foo'), 'mszqc bcfqr')
        self.assertEqual(vigenere.cifra('foo', 'bar'), 'gof')
        self.assertEqual(vigenere.cifra('sfx', 'foobar'), 'xtl')
        self.assertEqual(vigenere.cifra('a    b', 'foo'), 'f    p')

    def test_descifra(self):
        self.assertEqual(vigenere.descifra('mszqc bcfqr', 'foo'), 'hello world')
        self.assertEqual(vigenere.descifra('gof', 'bar'), 'foo')
        self.assertEqual(vigenere.descifra('xtl', 'foobar'), 'sfx')
        self.assertEqual(vigenere.descifra('f    p', 'foo'), 'a    b')

if __name__ == "__main__":
    unittest.main()