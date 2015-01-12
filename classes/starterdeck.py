'''##########################################################
   # StarterDeck CLASS -> defines the magic cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

from cards.magiccard import MagicCard
from cards.trapcard import TrapCard
from cards.creaturecard import CreatureCard
from cards.actioncard import ActionCard
from cards.weapon import Weapon
from cards.armor import Armor


class StarterDeck:

    magic = MagicCard()
    trap = TrapCard()
    creature = CreatureCard()
    action = ActionCard()
    weapon = Weapon()
    armor = Armor()

    magic_cards = {"name": magic.name("Wiseman"),
                    "type" : magic.magic_type("physical"),
                    "image" : "res/img/wiseman.png"}

    """trap_cards =
    creature_cards =
    action_cards =
    weapon_cards =
    armor_cards ="""


    def show(self):
        pass
