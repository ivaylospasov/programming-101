import unittest

from unique_words_count import unique_words_count


class UniqueWordsCountTest(unittest.TestCase):

    def test_if_the_result_is_correct(self):
        self.assertEqual(3, unique_words_count(
            ["apple", "banana", "apple", "pie"]))

    def test_if_the_result_is_zero_if_the_list_is_empty(self):
            self.assertEqual(0, unique_words_count([]))

if __name__ == '__main__':
    unittest.main()
