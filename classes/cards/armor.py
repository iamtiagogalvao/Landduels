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

    def initialize_card(self, *args, **kwargs):
        super(Armor, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Armor
        self.armor_type = kwargs["armor_type"] if "armor_type" in kwargs else ArmorTypes.Invalid

    def __repr__(self):
        armor_types= ArmorTypes.__dict__
        return "{0}\nArmor Type: {1}".format(
            super(Armor, self).__repr__(),
            list(armor_types)[armor_types.values().index(self.armor_type)])