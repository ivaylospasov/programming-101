from weapon import Weapon


class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._MAX_HEALTH = health
        self.weapon = {}

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.get_health() > 0:
            return True
        else:
            return False

    def take_damage(self, damage_points):
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points
        return self.health

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        if self.health + healing_points > self._MAX_HEALTH:
            self.health = self._MAX_HEALTH
        return True

    def has_weapon(self):
        if len(self.weapon) > 0:
            return True
        return False

    def equip_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon['weapon'] = Weapon.type
