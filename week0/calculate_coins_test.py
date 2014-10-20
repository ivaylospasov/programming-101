import unittest

from calculate_coins import calculate_coins


class CalculateCoinsTest(unittest.TestCase):

    def test_if_result_is_dictionary(self):
        self.assertNotEqual({}, calculate_coins(8.94))

    def test_if_the_result_is_ok(self):
        self.assertEqual({100: 1, 20: 1, 5: 1}, calculate_coins(1.25))

    def test_if_money_to_change_are_zero(self):
        self.assertEqual({}, calculate_coins(0))


if __name__ == '__main__':
    unittest.main()
