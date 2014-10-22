from random import random


class Weapon:

    def __init__(self, type, damage, csp):
        self.type = type
        self.damage = damage
        self.csp = csp

    def critical_hit(self):
        random_number = random()
        if random_number > self.csp:
            return False
        return True
