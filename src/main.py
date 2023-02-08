from AllWeapons import *
from ClassUser import User


user = User(1)
knife = Knife()

user.attack()

user.take_item(knife)
user.attack()

user.switch_item()
user.attack()

knife = Knife()
user.take_item(knife)
user.attack()

knife = Knife()
user.take_item(knife)
knife = None

user.switch_item()
user.attack()

crossbow = Crossbow()
user.take_item(crossbow)
print(user.weapons)

user.attack()
user.switch_item()
user.attack()

crossbow = Crossbow()
user.take_item(crossbow)
crossbow = None
print(user.weapons)
user.attack()

user.switch_item()
user.attack()

user.switch_item()
user.attack()

bow = Bow()
user.take_item(bow)

user.attack()
user.switch_item()
user.attack()

user.switch_item()
user.attack()

bow = Bow()
user.take_item(bow)
bow = None
user.attack()
