'''##########################################################
   # TrapCard CLASS -> defines the trap cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

from cards.card import Card

class TrapCard(Card):

    def __init__(self, image):
        super(TrapCard, self).__init__(image)

    trap_types = ("player", "enemy")

    def trap_type(self, trap):
        """Defines the type of trap the card has"""
        if trap not in self.trap_types:
           print "the trap is not known"
        return str(trap)
