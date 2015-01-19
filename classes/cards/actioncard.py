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

    def verify_args(self, *args, **kwargs):
        super(ActionCard, self).verify_args(*args, **kwargs)

        self.card_type = CardTypes.Action

        if kwargs.has_key("action_type"):
            self.action_type = kwargs["action_type"]
        else:
            self.action_type = ActionTypes.Invalid

    def __repr__(self):
        return "{0}\nAction Type: {1}".format(
            super(ActionCard, self).__repr__(),
            list(ActionTypes.__dict__)[ActionTypes.__dict__.values().index(self.action_type)])
