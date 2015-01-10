'''##########################################################
   # Armor CLASS -> defines the armor cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''
import card

class Armor(card.Card):

	
    armor_types = ("light", "heavy", "magic")
	
    def armor_type(self, armor):
        """Defines the type of armor the card has"""
        if armor not in self.armor_types:
           print "the armor type is not known"
        return str(armor)