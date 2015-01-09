import sys
sys.path.append("classes/cards/")

from card import*
from magiccard import*
from trapcard import*
from creaturecard import*
from actioncard import*

# ------>>>> The code below is an example of the class methods!

magic = MagicCard()
trap = TrapCard()
creature = CreatureCard()

#card types can be:
print "CARD TYPES:", Card.card_types

#creature types can be:
print "CREATURE TYPES:", CreatureCard.creature_types

#trap types can be:
print "TRAP TYPES:", TrapCard.trap_types

#action card types can be:
print "ACTION CARD TYPES:", ActionCard.action_types

#magic card types can be:
print "MAGIC CARD TYPES:", MagicCard.magic_types


#Defining a creature using array
badcobra = [creature.name("Bad Cobra"),
creature.card_type("creature"),
creature.creature_type("animal"),
creature.atack(5),
creature.defense(3)]

print "\n\n", badcobra


#Defining a creature using array
magicpunishment = [trap.name("Magic Punishment"),
trap.card_type("trap"),
]

print "\n\n", magicpunishment




