'''##########################################################
   # Card CLASS -> This is the main class for cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

import pygame
import uuid
from pygame.sprite import Sprite
from pygame.sprite import Rect
from util.enum import enum

CardTypes = enum("Invalid", "Creature", "Magic", "Trap", "Action", "Armor", "Weapon")

class Card(Sprite):

    def __init__(self, *args, **kwargs):
        super(Card, self).__init__()
        self.initialize_card(*args, **kwargs)

    def scale(self, factor):
        self._scale = factor
        self.image = self.card.copy()
        self.image = pygame.transform.rotozoom(self.image, self._angle, factor)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def rotate(self, angle):
        self._angle = angle
        self.image = self.card.copy()
        self.image = pygame.transform.rotozoom(self.image, angle, self._scale)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def position(self, x, y):
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def tint_surface(self, surface, colour, original=None ):
        tintSurf = pygame.Surface( surface.get_size()).convert_alpha()
        tintSurf.fill( colour )
        if original != None:
            surface.blit( original, (0,0) )
        surface.blit( tintSurf, (0,0), special_flags=pygame.BLEND_RGB_MULT )

    def initialize_card(self, *args, **kwargs):
        self.card_id = uuid.uuid1()
        self.card = pygame.image.load("res/img/blank_card.png").convert_alpha()
        self.tint = tuple(kwargs["tint"]) if "tint" in kwargs else (0,0,0,0)
        self.tint_surface(self.card, self.tint, self.card)

        self.card_type = kwargs["card_type"] if "card_type" in kwargs else CardTypes.Invalid
        self.mana_cost = kwargs["mana_cost"] if "mana_cost" in kwargs else 0
        self.image_path = kwargs["image"] if "image" in kwargs else "res/img/wiseman.png"
        self._image = pygame.image.load(self.image_path).convert()
        self._image = pygame.transform.scale(self._image, (328,242))

        self.card.blit(self._image, Rect((36,68),(242,328)))

        self.card_name = kwargs["card_name"] if "card_name" in kwargs else "Unnamed"

        font = pygame.font.Font("res/fonts/Goudy Mediaeval DemiBold.ttf", 24)
        text = font.render(self.card_name, 1, (10, 10, 10))
        self.card.blit(text, Rect((36,34), text.get_size()))

        self.attack = kwargs["attack"] if "attack" in kwargs else 0
        self.defense = kwargs["defense"] if "defense" in kwargs else 0

        # remaining defaults.
        self.image = self.card.copy()
        self.rect = self.image.get_rect()
        self._scale = 1.0
        self._angle = 0.0
        self.y = 0
        self.x = 0

    def is_valid(self):
        return self.card_type != CardTypes.Invalid

    def __repr__(self):
        card_types= CardTypes.__dict__
        return "Card Name: {0}\nCard ID: {1}\nCard Image: {2}\nCard Type: {3}\nAttack: {4}\nDefense: {5}\nMana Cost: {6}".format(
            self.card_name,
            self.card_id,
            self.image_path,
            list(card_types)[card_types.values().index(self.card_type)],
            self.attack,
            self.defense,
            self.mana_cost)


ActionTypes = enum("Invalid", "Player", "Enemy")

class ActionCard(Card):

    def __init__(self, *args, **kwargs):
        super(ActionCard, self).__init__(*args, **kwargs)

    def initialize_card(self, *args, **kwargs):
        super(ActionCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Action
        self.action_type = ActionTypes.__dict__[kwargs["action_type"]] if "action_type" in kwargs else ActionTypes.Invalid

    def __repr__(self):
        action_types= ActionTypes.__dict__
        return "{0}\nAction Type: {1}".format(
            super(ActionCard, self).__repr__(),
            list(action_types)[action_types.values().index(self.action_type)])


ArmorTypes = enum("Invalid", "Light", "Heavy", "Magic")

class Armor(Card):

    def __init__(self, *args, **kwargs):
        super(Armor, self).__init__(*args, **kwargs)

    def initialize_card(self, *args, **kwargs):
        super(Armor, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Armor
        self.armor_type = ArmorTypes.__dict__[kwargs["armor_type"]] if "armor_type" in kwargs else ArmorTypes.Invalid

    def __repr__(self):
        armor_types= ArmorTypes.__dict__
        return "{0}\nArmor Type: {1}".format(
            super(Armor, self).__repr__(),
            list(armor_types)[armor_types.values().index(self.armor_type)])


CreatureTypes = enum("Invalid", "Human", "Animal", "MagicBeing", "ShadowBeing", "LightBeing")

class CreatureCard(Card):

    def __init__(self, *args, **kwargs):
        super(CreatureCard, self).__init__(*args, **kwargs)

    def initialize_card(self, *args, **kwargs):
        super(CreatureCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Creature
        self.creature_type = CreatureTypes.__dict__[kwargs["creature_type"]] if "creature_type" in kwargs else CreatureTypes.Invalid

    def __repr__(self):
        creature_types= CreatureTypes.__dict__
        return "{0}\nCreature Type: {1}".format(
            super(CreatureCard, self).__repr__(),
            list(creature_types)[creature_types.values().index(self.creature_type)])


MagicTypes = enum("Invalid", "Physical", "Magical")

class MagicCard(Card):

    def __init__(self, *args, **kwargs):
        super(MagicCard, self).__init__(*args, **kwargs)

    def initialize_card(self, *args, **kwargs):
        super(MagicCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Magic
        self.magic_type = MagicTypes.__dict__[kwargs["magic_type"]] if "magic_type" in kwargs else MagicTypes.Invalid

    def __repr__(self):
        magic_types= MagicTypes.__dict__
        return "{0}\nMagic Type: {1}".format(
            super(MagicCard, self).__repr__(),
            list(magic_types)[magic_types.values().index(self.magic_type)])


TrapTypes = enum("Invalid", "Player", "Enemy")

class TrapCard(Card):

    def __init__(self, *args, **kwargs):
        super(TrapCard, self).__init__(*args, **kwargs)

    def initialize_card(self, *args, **kwargs):
        super(TrapCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Trap
        self.trap_type = TrapTypes.__dict__[kwargs["trap_type"]] if "trap_type" in kwargs else TrapTypes.Invalid

    def __repr__(self):
        trap_types= TrapTypes.__dict__
        return "{0}\nTrap Type: {1}".format(
            super(TrapCard, self).__repr__(),
            list(trap_types)[trap_types.values().index(self.trap_type)])


WeaponTypes = enum("Invalid", "Blade", "Axe", "MagicPole")

class Weapon(Card):

    def __init__(self, *args, **kwargs):
        super(Weapon, self).__init__(*args, **kwargs)

    def initialize_card(self, *args, **kwargs):
        super(Weapon, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Weapon
        self.weapon_type = WeaponTypes.__dict__[kwargs["weapon_type"]] if "weapon_type" in kwargs else WeaponTypes.Invalid

    def __repr__(self):
        weapon_types= WeaponTypes.__dict__
        return "{0}\nWeapon Type: {1}".format(
            super(Weapon, self).__repr__(),
            list(weapon_types)[weapon_types.values().index(self.weapon_type)])

