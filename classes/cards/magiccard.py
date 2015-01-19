'''##########################################################
   # MagicCard CLASS -> defines the magic cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

from cards.card import Card

class MagicCard(Card):

    def __init__(self, image):
        super(MagicCard, self).__init__(image)

    magic_types = ("physical", "magical")

    def magic_type(self, magic):
        """Defines the type of magic the card has"""
        if magic not in self.magic_types:
            print "the magic type is not known"
        return str(magic)




