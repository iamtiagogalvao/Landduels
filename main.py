import sys
sys.path.append("classes/cards/")

from card import*
from magiccard import*
from trapcard import*
from creaturecard import*
from actioncard import*
from weapon import*
from armor import*

# ------>>>> The code below is an example of the class methods!

magic = MagicCard()
trap = TrapCard()
creature = CreatureCard()
weapon = Weapon()
armor = Armor()
actioncard = ActionCard()


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

#weapon types can be:
print "WEAPON TYPES CAN BE:", Weapon.weapon_types

#armor types can be:
print "ARMOR TYPES CAN BE:", Armor.armor_types


#Defining a creature using array
badcobra = [creature.name("Bad Cobra"),
            creature.card_type("creature"),
            creature.creature_type("animal"),
            creature.atack(5),
            creature.defense(3)]

print "\n\n", badcobra


#Defining a trap using array
magicpunishment = [trap.name("Magic Punishment"),
                    trap.card_type("trap"),
                    trap.trap_type("player")]

print "\n\n", magicpunishment

#Defining a magic card using array
lavawind = [magic.name("Lava Wind"),
            magic.card_type("magic"),
            magic.magic_type("physical")]


print "\n\n", lavawind


