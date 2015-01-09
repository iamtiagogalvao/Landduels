'''##########################################################
   # MagicCard CLASS -> defines the magic cards
   # Created: 2015 - 01 - 09 ||| Last review: 2015 - 01 - xx
   # Slaveworx, (add your credits here joe)
   #########################################################'''
import card

class MagicCard(card.Card):


    def power(self, power):
        """Defines the type of power the card has"""
        if power not in self.power_types:
           print "the power is not known"
        return power




