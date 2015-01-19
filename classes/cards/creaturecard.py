'''##########################################################
   # CreatureCard CLASS -> defines the creature cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

from cards.card import Card, CardTypes
from util.enum import enum

CreatureTypes = enum("Invalid", "Human", "Animal", "MagicBeing", "ShadowBeing", "LightBeing")

class CreatureCard(Card):

    def __init__(self, *args, **kwargs):
        super(CreatureCard, self).__init__(*args, **kwargs)

    def initialize_card(self, *args, **kwargs):
        super(CreatureCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Creature

        if kwargs.has_key("creature_type"):
            self.creature_type = kwargs["creature_type"]
        else:
            self.creature_type = CreatureTypes.Invalid

    def __repr__(self):
        creature_types= CreatureTypes.__dict__
        return "{0}\nCreature Type: {1}".format(
            super(CreatureCard, self).__repr__(),
            list(creature_types)[creature_types.values().index(self.creature_type)])

