from AllWeapons import *


class User:
    __id = 0
    __activ_weapon = None
    __count_switch_weapon = 0
    __weapons = []

    def __init__(self, user_id):
        if type(user_id) == int:
            self.__id = int(user_id)
        else:
            raise ValueError("Error int")

    def take_item(self, weapon):
        if len(self.__weapons) != Weapon.get_weapons():
            if isinstance(weapon, Weapon):
                if len(self.__weapons) != 0:
                    boolean = True

                    for weapon1 in self.__weapons:
                        if type(weapon) == type(weapon1):
                            boolean = False
                            print("you have this weapon")
                            break

                    if boolean:
                        self.__weapons.append(weapon)
                        print("weapon is took 2")
                else:
                    self.__weapons.append(weapon)

                    if self.__activ_weapon is None:
                        self.__activ_weapon = self.__weapons[0]
                        print("if None")

                    print("weapon is took 1")
            else:
                print("This is not weapon")
        else:
            print("Inventory is full")

    def switch_item(self):
        if self.__count_switch_weapon != len(self.__weapons) - 1:
            self.__count_switch_weapon += 1
            self.__activ_weapon = self.__weapons[self.__count_switch_weapon]
        else:
            self.__count_switch_weapon = 0
            self.__activ_weapon = self.__weapons[self.__count_switch_weapon]

        print("switch weapon")

    def attack(self):
        if self.__activ_weapon is None:
            print("weapon is None")
        else:
            self.__activ_weapon.attack()

    @property
    def id(self):
        return self.__id

    @property
    def weapons(self):
        return self.__weapons

    @property
    def number_of_weapons(self):
        return len(self.__weapons)
