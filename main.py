import pygame
from cards.card import *
from cards.magiccard import *
from cards.trapcard import *
from cards.creaturecard import *
from cards.actioncard import *
from cards.weapon import *
from cards.armor import *

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
print "ARMOR TYPES CAN BE:", ArmorTypes.values()


# Define creature with CreatureCard class
badcobra = CreatureCard(
    name="Bad Cobra",
    card_type=CardTypes.Creature,
    creature_type=CreatureTypes.Animal,
    attack=5,
    defense=3)

print "\n\n", badcobra


#Defining a trap using TrapCard
magicpunishment = TrapCard(
    name="Magic Punishment",
    card_type=CardTypes.Trap,
    trap_type=TrapTypes.Player)

print "\n\n", magicpunishment

#Defining a magic card using MagicCard
lavawind = MagicCard(
    name="Lava Wind",
    card_type=CardTypes.Magic,
    magic_type=MagicTypes.Physical)

print "\n\n", lavawind


