import unittest

from spam_and_eggs import prepare_meal


class SpamAndEggsTest(unittest.TestCase):

    def test_if_number_is_not_equal_to_3_on_power_of_n_or_cant_be_divided_by_5(self):
        self.assertEqual("", prepare_meal(4))

    def test_if_number_is_not_equal_to_3_on_power_of_n_and_can_be_divided_by_5(self):
        self.assertEqual("eggs", prepare_meal(25))

    def test_if_number_is_equal_to_3_on_power_of_n(self):
        self.assertEqual("spam spam spam ", prepare_meal(27))

    def test_if_number_can_be_divided_by_5(self):
        self.assertEqual("eggs", prepare_meal(25))

    def test_if_number_is_equal_to_3_on_power_of_n_and_can_be_divided_by_5(self):
        self.assertEqual("spam spam and eggs", prepare_meal(45))

if __name__ == '__main__':
    unittest.main()
