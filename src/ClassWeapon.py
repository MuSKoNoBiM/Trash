class Weapon:
    __weapons = 0

    @classmethod
    def _add_weapon(cls):
        cls.__weapons += 1

    @classmethod
    def get_weapons(cls):
        return cls.__weapons

    def attack(self):
        raise NotImplementedError
