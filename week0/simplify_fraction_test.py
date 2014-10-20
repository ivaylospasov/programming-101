import unittest

from simplify_fraction import simplify_fraction, dividers


class SimplifyFractionTest(unittest.TestCase):

    def test_check_the_dividers_of_the_first_number_of_the_fraction(self):
        self.assertEqual([63, 21, 9, 7, 3, 1], dividers(63))

    def test_check_false_number_of_dividers_of_the_first_number_of_the_fraction(self):
        self.assertNotEqual([63, 21, 9, 7, 3], dividers(63))

    def test_check_the_simlify_fraction_function_with_false_answer(self):
        self.assertNotEqual((7, 22), simplify_fraction((63, 462)))

    def test_check_the_simlify_fraction_function_with_true_answer(self):
        self.assertEqual((3, 22), simplify_fraction((63, 462)))


if __name__ == '__main__':
    unittest.main()
