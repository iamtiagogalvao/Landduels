'''##########################################################
   # StarterDeck CLASS -> defines the magic cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''
import sys
sys.path.append("cards/")

from card import*
from magiccard import*
from trapcard import*
from creaturecard import*
from actioncard import*
from weapon import*
from armor import*


class StarterDeck:


    magic = MagicCard()
    trap = TrapCard()
    creature = CreatureCard()
    action = ActionCard()
    weapon = Weapon()
    armor = Armor()

    magic_cards = {"name": magic.name("Wiseman"),
                    "type" : magic.magic_type("physical")
                    "image" : "res/img/wiseman.png"}

    """trap_cards =
    creature_cards =
    action_cards =
    weapon_cards =
    armor_cards ="""


    def show(self):
        pass
