import unittest

from count_words import count_words


class CountWordsTest(unittest.TestCase):

    def test_if_the_list_is_not_empty(self):
        self.assertNotEqual({}, count_words([
            "apple", "banana", "apple", "pie", "banana"]))

    def test_if_the_word_count_is_true(self):
        self.assertEqual({"apple": 2, "banana": 2, "pie": 1}, count_words([
            "apple", "banana", "apple", "pie", "banana"]))

    def test_if_list_is_empty(self):
        self.assertEqual({}, count_words([]))

if __name__ == '__main__':
    unittest.main()
