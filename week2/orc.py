from entity import Entity


class Orc(Entity):
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.__set_selfberserk_factor(berserk_factor)

    def __set_selfberserk_factor(self, berserk_factor):
        if berserk_factor > 1 and berserk_factor < 2:
            self.berserk_factor = berserk_factor
        else:
            raise ValueError
