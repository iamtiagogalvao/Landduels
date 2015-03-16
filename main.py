import pygame
from cards.card import *
from cards.deck import Deck

# ------>>>> The code below is an example of the class methods!

# For whatever reason, cards having images requires pygame display to be initialized.
pygame.init()
pygame.display.set_mode((800, 600), pygame.HWSURFACE)

#card types can be:
print "CARD TYPES:", CardTypes.values()

#creature types can be:
print "CREATURE TYPES:", CreatureTypes.values()

#trap types can be:
print "TRAP TYPES:", TrapTypes.values()

#action card types can be:
print "ACTION CARD TYPES:", ActionTypes.values()

#magic card types can be:
print "MAGIC CARD TYPES:", MagicTypes.values()

#weapon types can be:
print "WEAPON TYPES CAN BE:", WeaponTypes.values()

#armor types can be:
print "ARMOR TYPES CAN BE:", ArmorTypes.values(), "\n"

test_deck = Deck('classes/decks/starterdeck.json')

for card in test_deck.cards:
    print card, "\n"

