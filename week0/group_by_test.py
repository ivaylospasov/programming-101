import unittest

from group_by import groupby


class GroupByTest(unittest.TestCase):

    def test_if_second_arg_is_empty_list(self):
        self.assertEqual({}, groupby(lambda x: 'odd' if x % 2 else 'even', []))

    def test_if_the_result_is_not_empty_if_list_is_not_empty(self):
        self.assertNotEqual({}, groupby(lambda x: 'odd' if x % 2 else 'even', [
            1, 2, 3, 5, 8, 9, 10, 12]))

    def test_if_lambda_is_correct_function(self):
        self.assertEqual({'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]},
                         groupby(lambda x: 'odd' if x % 2 else 'even', [
                             1, 2, 3, 5, 8, 9, 10, 12]))


if __name__ == '__main__':
    unittest.main()
