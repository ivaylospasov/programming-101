import unittest

from fight import Fight
from hero import Hero
from orc import Orc
from weapon import Weapon


class FightTest(unittest.TestCase):

    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")
        self.torug_orc = Orc("Torug", 100, 1.2)
        self.new_fight = Fight(self.bron_hero, self.torug_orc)
        self.axe = Weapon("Axe", 20, 0.2)
        self.sword = Weapon("Sword", 12, 0.7)
        self.bron_hero.equip_weapon(self.sword)
        self.torug_orc.equip_weapon(self.axe)

    def test_init(self):
        self.assertEqual(self.new_fight.orc, self.torug_orc)
        self.assertEqual(self.new_fight.hero, self.bron_hero)

    def test_who_is_first(self):
        first_entity = self.new_fight.who_is_first()
        self.assertIn(first_entity, [self.bron_hero, self.torug_orc])

    def test_fight(self):
        self.new_fight.simulate_battle()
        self.assertFalse(self.torug_orc.is_alive() and self.bron_hero.is_alive())

    def test_fight_with_no_weapons(self):
        self.torug_orc.weapon = None
        self.new_fight.simulate_battle()
        self.assertFalse(self.torug_orc.is_alive())

if __name__ == '__main__':
    unittest.main()
