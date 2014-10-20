import unittest

from is_an_bn import is_an_bn


class AnBnWordTest(unittest.TestCase):

    def test_with_empty_word(self):
        self.assertEqual(True, is_an_bn(''))

    def test_word_with_odd_number_of_letters(self):
        self.assertFalse(is_an_bn('aaabb'))

    def test_word_with_even_number_of_letters_with_defferent_halfs(self):
        self.assertFalse(is_an_bn('ababab'))

    def test_word_with_even_number_of_letters_with_equal_halfs(self):
        self.assertTrue(is_an_bn('aaabbb'))

if __name__ == '__main__':
    unittest.main()
