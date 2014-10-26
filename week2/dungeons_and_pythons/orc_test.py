import unittest
from entity import Entity
from weapon import Weapon
import orc


class OrcTest(unittest.TestCase):

    def setUp(self):
        self.torug_orc = orc.Orc("Torug", 100, 1.2)

    def test_orc_init(self):
        self.assertEqual(self.torug_orc.berserk_factor, 1.2)

    def test_attack_with_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 1.2)
        self.torug_orc.equip_weapon(weapon)
        self.assertEqual(self.torug_orc.attack(), 30)


if __name__ == '__main__':
    unittest.main()
