'''##########################################################
   # Card CLASS -> This is the main class for cards
   # Created: 2015 - 01 - 09 ||| Last review: 2015 - 01 - xx
   # Slaveworx, (add your credits here joe)
   #########################################################'''

class Card:


    card_types = ("creature", "magic", "trap", "action", "armor", "weapon")

    def atack(self, atack):
        return int(atack)

    def defense(self, defense):
        return int(defense)

    def name(self, name):
        return str(name)

    def card_type(self, card_type):
        if card_type not in self.card_types:
           print "the card type is not known"
        return str(card_type)
