'''##########################################################
   # MagicCard CLASS -> defines the magic cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

from cards.card import Card, CardTypes
from util.enum import enum

MagicTypes = enum("Invalid", "Physical", "Magical")

class MagicCard(Card):

    def __init__(self, *args, **kwargs):
        super(MagicCard, self).__init__(*args, **kwargs)

    def initialize_card(self, *args, **kwargs):
        super(MagicCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Magic

        if kwargs.has_key("magic_type"):
            self.magic_type = kwargs["magic_type"]
        else:
            self.magic_type = MagicTypes.Invalid

    def __repr__(self):
        magic_types= MagicTypes.__dict__
        return "{0}\nMagic Type: {1}".format(
            super(MagicCard, self).__repr__(),
            list(magic_types)[magic_types.values().index(self.magic_type)])




