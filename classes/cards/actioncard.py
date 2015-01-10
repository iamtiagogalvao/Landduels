'''##########################################################
   # ActionCard CLASS -> defines the action cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

import card

class ActionCard(card.Card):


    action_types= ("player", "enemy")

    def action_type(self, action):
        """Defines the type of action the card has"""
        if action not in self.action_types:
           print "the action card type is not known"
        return str(action)
