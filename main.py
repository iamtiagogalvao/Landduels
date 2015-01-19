import pygame
from cards.card import *
from cards.magiccard import *
from cards.trapcard import *
from cards.creaturecard import *
from cards.actioncard import *
from cards.weapon import *
from cards.armor import *
from util.enum import values

# ------>>>> The code below is an example of the class methods!

# For whatever reason, cards having images requires pygame display to be initialized.
pygame.init()
pygame.display.set_mode((800, 600), pygame.HWSURFACE)

#card types can be:
print "CARD TYPES:", values(CardTypes)

#creature types can be:
print "CREATURE TYPES:", values(CreatureTypes)

#trap types can be:
print "TRAP TYPES:", values(TrapTypes)

#action card types can be:
print "ACTION CARD TYPES:", values(ActionTypes)

#magic card types can be:
print "MAGIC CARD TYPES:", values(MagicTypes)

#weapon types can be:
print "WEAPON TYPES CAN BE:", values(WeaponTypes)

#armor types can be:
print "ARMOR TYPES CAN BE:", values(ArmorTypes)


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


