'''##########################################################
   # Weapon CLASS -> defines the weapon cards
   # Created: 2015 - 01 - 09 ||| Last review: 2015 - 01 - xx
   # Slaveworx, (add your credits here joe)
   #########################################################'''
import card

class Weapon(card.Card):

	
    weapon_types = ("blade", "axe", "magic_pole")
	
    def weapon_type(self, weapon):
        """Defines the type of weapon the card has"""
        if weapon not in self.weapon_types:
           print "the weapon type is not known"
        return str(weapon)


