'''##########################################################
   # TrapCard CLASS -> defines the trap cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

from cards.card import Card, CardTypes
from util.enum import enum

TrapTypes = enum("Invalid", "Player", "Enemy")

class TrapCard(Card):

    def __init__(self, *args, **kwargs):
        super(TrapCard, self).__init__(*args, **kwargs)

    def initialize_card(self, *args, **kwargs):
        super(TrapCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Trap

        if kwargs.has_key("trap_type"):
            self.trap_type = kwargs["trap_type"]
        else:
            self.trap_type = TrapTypes.Invalid

    def __repr__(self):
        return "{0}\nTrap Type: {1}".format(
            super(TrapCard, self).__repr__(),
            list(TrapTypes.__dict__)[TrapTypes.__dict__.values().index(self.trap_type)])
