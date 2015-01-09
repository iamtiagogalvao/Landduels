import sys
sys.path.append("classes/cards/")

from magiccard import*
from trapcard import*
from creaturecard import*

# ------>>>> The code below is an example of the class methods!

magic = MagicCard()
trap = TrapCard()
creature = CreatureCard()

all= [creature.name("Bad Cobra"),
creature.card_type("animal"),
creature.creature_type("animal"),
creature.atack(5),
creature.defense(3)]

print all




