'''##########################################################
   # Armor CLASS -> defines the armor cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

from cards.card import Card, CardTypes
from util.enum import enum

ArmorTypes = enum("Invalid", "Light", "Heavy", "Magic")

class Armor(Card):

    def __init__(self, *args, **kwargs):
        super(Armor, self).__init__(*args, **kwargs)

    def verify_args(self, *args, **kwargs):
        super(Armor, self).verify_args(*args, **kwargs)

        self.card_type = CardTypes.Armor

        if kwargs.has_key("armor_type"):
            self.armor_type = kwargs["armor_type"]
        else:
            self.armor_type = ArmorTypes.Invalid

    def __repr__(self):
        return "{0}\nArmor Type: {1}".format(
            super(Armor, self).__repr__(),
            list(ArmorTypes.__dict__)[ArmorTypes.__dict__.values().index(self.armor_type)])