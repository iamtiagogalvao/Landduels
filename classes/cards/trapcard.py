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
        self.trap_type = kwargs["trap_type"] if "trap_type" in kwargs else TrapTypes.Invalid

    def __repr__(self):
        trap_types= TrapTypes.__dict__
        return "{0}\nTrap Type: {1}".format(
            super(TrapCard, self).__repr__(),
            list(trap_types)[trap_types.values().index(self.trap_type)])
