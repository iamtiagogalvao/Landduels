'''##########################################################
   # ActionCard CLASS -> defines the creature cards
   # Created: 2015 - 01 - 09 ||| Last review: 2015 - 01 - xx
   # Slaveworx, (add your credits here joe)
   #########################################################'''

import card

class ActionCard(card.Card):


    action_types= ("player", "enemy")

    def action_type(self, action_type):
        """Defines the type of being the card has"""
        if action_type not in self.action_types:
           print "the action card type is not known"
        return str(action_type)
