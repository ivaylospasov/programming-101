import unittest

from sort_fractions import tuples_divisions, combine_tuples_and_divisions, sort_fractions


class SortFractionsTest(unittest.TestCase):

    def test_if_tuples_divisions_returns_list_of_correct_tuples_divisions(self):
        self.assertEqual([0.8333333333333334,
                          3.142857142857143],
                         tuples_divisions([(5, 6), (22, 7)]))

    def test_combine_tuples_and_divisions_for_returning_dictionary_with_divisions_for_keys_and_tuples_for_values(self):
        self.assertEqual({0.8333333333333334: (5, 6),
                          3.142857142857143: (22, 7)},
                         combine_tuples_and_divisions([(5, 6), (22, 7)]))

    def test_combine_tuples_and_divisions_for_returning_dictionary_with_tuples_for_keys_and_divisions_for_values(self):
        self.assertNotEqual({(5, 6): 0.8333333333333334,
                             (22, 7): 3.142857142857143},
                            combine_tuples_and_divisions([(5, 6), (22, 7)]))

    def test_if_the_final_list_is_sorted_by_tuples_divisions(self):
        self.assertEqual([(5, 6), (22, 7)], sort_fractions([(5, 6), (22, 7)]))

    def test_if_the_final_list_is_sorted_correctly_if_replace_tuples_places(self):
        self.assertEqual([(5, 6), (22, 7)], sort_fractions([(22, 7), (5, 6)]))

if __name__ == '__main__':
    unittest.main()
