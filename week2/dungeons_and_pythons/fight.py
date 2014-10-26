from random import random
from entity import Entity
from weapon import Weapon
from orc import Orc
from hero import Hero


class Fight():
    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def who_is_first(self):
        coin = random()
        if coin < 0.5:
            return self.hero
        else:
            return self.orc

    def simulate_battle(self):
        attaker = self.who_is_first()
        if attaker == self.hero:
            attaker = self.hero
            attaked = self.orc
        else:
            attaker = self.orc
            attaked = self.hero

        while self.orc.is_alive() and self.hero.is_alive():
            damage = attaker.attack()
            attaker.take_damage(damage)
            attaked.take_damage(damage)
            attaker, attaked = attaked, attaker
