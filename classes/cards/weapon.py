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

    def initialize_card(self, *args, **kwargs):
        super(Weapon, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Weapon

        if kwargs.has_key("weapon_type"):
            self.weapon_type = kwargs["weapon_type"]
        else:
            self.weapon_type = WeaponTypes.Invalid

    def __repr__(self):
        weapon_types= WeaponTypes.__dict__
        return "{0}\nWeapon Type: {1}".format(
            super(Weapon, self).__repr__(),
            list(weapon_types)[weapon_types.values().index(self.weapon_type)])