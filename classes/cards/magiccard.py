'''##########################################################
   # MagicCard CLASS -> defines the magic cards
   # Created: 2015 - 01 - 09 ||| Last review: 2015 - 01 - xx
   # Slaveworx, (add your credits here joe)
   #########################################################'''
import card

class MagicCard(card.Card):

	
    magic_types = ("physical", "magical", "affect_player", "affect_enemy")
	
    def power(self, magic):
        """Defines the type of power the card has"""
        if magic not in self.magic_types:
           print "the magic type is not known"
        return str(magic)




