'''##########################################################
   # ActionCard CLASS -> defines the action cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

from cards.card import Card, CardTypes
from util.enum import enum

ActionTypes = enum("Invalid", "Player", "Enemy")

class ActionCard(Card):

    def __init__(self, *args, **kwargs):
        super(ActionCard, self).__init__(*args, **kwargs)

    def initialize_card(self, *args, **kwargs):
        super(ActionCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Action
        self.action_type = kwargs["action_type"] if "action_type" in kwargs else ActionTypes.Invalid

    def __repr__(self):
        action_types= ActionTypes.__dict__
        return "{0}\nAction Type: {1}".format(
            super(ActionCard, self).__repr__(),
            list(action_types)[action_types.values().index(self.action_type)])
