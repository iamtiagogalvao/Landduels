'''##########################################################
   # Weapon CLASS -> defines the weapon cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

from cards.card import Card

class Weapon(Card):

    weapon_types = ("blade", "axe", "magic_pole")

    def weapon_type(self, weapon):
        """Defines the type of weapon the card has"""
        if weapon not in self.weapon_types:
            print "the weapon type is not known"
        return str(weapon)


