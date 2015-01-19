'''##########################################################
   # Weapon CLASS -> defines the weapon cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

from cards.card import Card, CardTypes
from util.enum import enum

WeaponTypes = enum("Invalid", "Blade", "Axe", "MagicPole")

class Weapon(Card):

    def __init__(self, *args, **kwargs):
        super(Weapon, self).__init__(*args, **kwargs)

    def verify_args(self, *args, **kwargs):
        super(Weapon, self).verify_args(*args, **kwargs)

        self.card_type = CardTypes.Weapon

        if kwargs.has_key("weapon_type"):
            self.weapon_type = kwargs["weapon_type"]
        else:
            self.weapon_type = WeaponTypes.Invalid

    def __repr__(self):
        return "{0}\nWeapon Type: {1}".format(
            super(Weapon, self).__repr__(),
            list(WeaponTypes.__dict__)[WeaponTypes.__dict__.values().index(self.weapon_type)])