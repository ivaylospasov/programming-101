import unittest

import entity

from weapon import Weapon


class EntityTest(unittest.TestCase):

    def setUp(self):
        self.some_entity = entity.Entity("Bobo", 100)

    def test_entity_init(self):
        self.assertEqual(self.some_entity.name, 'Bobo')
        self.assertEqual(self.some_entity.health, 100)

    def test_entity_get_health(self):
        self.assertEqual(self.some_entity.get_health(), 100)

    def test_entity_is_alive(self):
        self.assertTrue(self.some_entity.is_alive())
        self.some_entity.health = 0
        self.assertFalse(self.some_entity.is_alive())

    def test_entity_take_damage_int(self):
        self.assertEqual(self.some_entity.take_damage(30), 70)

    def test_entity_take_damage_float(self):
        self.assertEqual(self.some_entity.take_damage(29.5), 70.5)

    def test_entity_take_damage_over_death_entity(self):
        self.assertEqual(self.some_entity.take_damage(150), 0)

    def test_entity_take_healing_of_the_dead_entity(self):
        self.some_entity.health = 0
        self.assertFalse(self.some_entity.take_healing(50))

    def test_entity_take_healing_of_alive_entity(self):
        self.assertTrue(self.some_entity.take_healing(50))

    def test_it_entity_has_no_weapon(self):
        self.assertFalse(self.some_entity.has_weapon())

    def test_if_entity_has_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.some_entity.equip_weapon(weapon)
        self.assertTrue(self.some_entity.has_weapon())

    def test_equip_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.assertEqual(self.some_entity.equip_weapon(weapon),
                         {'weapon': {'type': 'Mighty Axe', 'damage': 25, 'csp': 0.2}})

    def test_equip_with_another_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.some_entity.equip_weapon(weapon)
        weapon = Weapon("Magic Sword", 20, 0.3)
        self.assertEqual(self.some_entity.equip_weapon(weapon),
                         {'weapon': {'type': 'Magic Sword', 'damage': 20, 'csp': 0.3}})

    def test_attack_with_no_weapon(self):
        self.assertEqual(self.some_entity.attack(), 0)

    def test_attack_with_weapon(self):
        weapon = Weapon("Mighty Axe", 25, 0.2)
        self.some_entity.equip_weapon(weapon)
        self.assertEqual(self.some_entity.attack(), 25)

if __name__ == '__main__':
    unittest.main()
