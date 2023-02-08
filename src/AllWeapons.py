from ClassWeapon import Weapon


class Crossbow (Weapon):
    Weapon._add_weapon()

    def attack(self):
        print("Crossbow: Attack")


class Knife (Weapon):
    Weapon._add_weapon()

    def attack(self):
        print("Knife: Attack")


class Bow (Weapon):
    Weapon._add_weapon()

    def attack(self):
        print("Bow: Attack")
