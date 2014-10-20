import unittest

from biggest_difference import biggest_difference


class BiggestDifferenceTestClass(unittest.TestCase):

    def test_if_the_result_is_negative_number(self):
        self.assertTrue(biggest_difference([-2, 0, -7, 5]) < 0)


if __name__ == '__main__':
    unittest.main()
