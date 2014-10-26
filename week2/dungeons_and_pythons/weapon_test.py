import unittest

from weapon import Weapon


class WeaponTest(unittest.TestCase):
    def setUp(self):
        self.default_weapon = Weapon('Mighty Axe', 25, 0.2)

    def test_init_weapon(self):
        self.assertEqual(self.default_weapon.type, 'Mighty Axe')
        self.assertEqual(self.default_weapon.damage, 25)
        self.assertEqual(self.default_weapon.critical_strike_percent, 0.2)

    def test_critical_hit(self):
        results = []
        for x in range(1000):
            results.append(self.default_weapon.critical_hit())
        self.assertTrue(True in results)
        self.assertTrue(False in results)


if __name__ == '__main__':
    unittest.main()
