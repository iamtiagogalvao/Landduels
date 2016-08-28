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

    def tint_surface(self, surface, colour, original=None):
        tint_surf = pygame.Surface(surface.get_size()).convert_alpha()
        tint_surf.fill(colour)
        if original is not None:
            surface.blit(original, (0, 0))
        surface.blit(tint_surf, (0, 0), special_flags=pygame.BLEND_RGB_MULT)

    def draw_wrapped_text(self, surface, text, color, rect, font, aa=False, bkg=None):
        rect = Rect(rect)
        y = rect.top
        line_spacing = -2

        # get the height of the font
        font_height = font.size("Tg")[1]

        while text:
            i = 1

            # determine if the row of text will be outside our area
            if y + font_height > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word
            if i > len(text):
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            surface.blit(image, (rect.left, y))
            y += font_height + line_spacing

            # remove the text we just blitted
            text = text[i:]

        return text

    def get_card_type_string(self):
        card_types = CardTypes.__dict__
        card_type_values = list(card_types.values())
        return str(list(card_types)[card_type_values.index(self.card_type)])

    def initialize_card(self, *args, **kwargs):
        self.card_id = uuid.uuid1()

        self.card = pygame.image.load("res/img/blank_card.png").convert_alpha()

        self.tint = tuple(kwargs["tint"]) if "tint" in kwargs else (0, 0, 0, 0)
        self.tint_surface(self.card, self.tint, self.card)

        self.card_type = CardTypes.__dict__[kwargs["card_type"]] if "card_type" in kwargs else CardTypes.Invalid
        self.card_type_description = self.get_card_type_string()

        self.mana_cost = kwargs["mana_cost"] if "mana_cost" in kwargs else 0
        self.image_path = kwargs["image"] if "image" in kwargs else "res/img/wiseman.png"
        self._image = pygame.image.load(self.image_path).convert()
        self._image = pygame.transform.scale(self._image, (328, 242))

        self.card.blit(self._image, Rect((36, 68), (328, 242)))

        self.card_name = kwargs["card_name"] if "card_name" in kwargs else "Unnamed"

        font = pygame.font.Font("res/fonts/Goudy Mediaeval DemiBold.ttf", 24)
        text = font.render(self.card_name, 1, (10, 10, 10))
        self.card.blit(text, Rect((38, 34), text.get_size()))

        self.card_description = kwargs["card_description"] if "card_description" else "Card description."

        font = pygame.font.Font("res/fonts/mplantin.ttf", 18)
        self.draw_wrapped_text(
            self.card, self.card_description, (10, 10, 10), Rect((36, 355), (320, 150)), font)

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
        return "Card Name: {0}\nCard ID: {1}\nCard Image: {2}\nCard Type: {3}\nAttack: {4}\nDefense: {5}\nMana Cost: {6}".format(
            self.card_name,
            self.card_id,
            self.image_path,
            self.get_card_type_string(),
            self.attack,
            self.defense,
            self.mana_cost)


ActionTypes = enum("Invalid", "Player", "Enemy")


class ActionCard(Card):
    def __init__(self, *args, **kwargs):
        super(ActionCard, self).__init__(*args, **kwargs)

    def get_action_type_string(self):
        action_types = ActionTypes.__dict__
        action_type_values = list(action_types.values())
        return str(list(action_types)[action_type_values.index(self.action_type)])

    def initialize_card(self, *args, **kwargs):
        super(ActionCard, self).initialize_card(*args, **kwargs)

        self.action_type = ActionTypes.__dict__[
            kwargs["action_type"]] if "action_type" in kwargs else ActionTypes.Invalid

        self.card_type_description += " -- "
        self.card_type_description += self.get_action_type_string()

        font = pygame.font.Font("res/fonts/Goudy Mediaeval DemiBold.ttf", 24)
        text = font.render(self.card_type_description, 1, (10, 10, 10))
        self.card.blit(text, Rect((38, 315), text.get_size()))

    def __repr__(self):
        return "{0}\nAction Type: {1}".format(
            super(ActionCard, self).__repr__(),
            self.get_action_type_string())


ArmorTypes = enum("Invalid", "Light", "Heavy", "Magic")


class ArmorCard(Card):
    def __init__(self, *args, **kwargs):
        super(ArmorCard, self).__init__(*args, **kwargs)

    def get_armor_type_string(self):
        armor_types = ArmorTypes.__dict__
        armor_type_values = list(armor_types.values())
        return str(list(armor_types)[armor_type_values.index(self.armor_type)])

    def initialize_card(self, *args, **kwargs):
        super(ArmorCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Armor
        self.armor_type = ArmorTypes.__dict__[kwargs["armor_type"]] if "armor_type" in kwargs else ArmorTypes.Invalid

        self.card_type_description += " -- "
        self.card_type_description += self.get_armor_type_string()

        font = pygame.font.Font("res/fonts/Goudy Mediaeval DemiBold.ttf", 24)
        text = font.render(self.card_type_description, 1, (10, 10, 10))
        self.card.blit(text, Rect((38, 315), text.get_size()))

    def __repr__(self):
        return "{0}\nArmor Type: {1}".format(
            super(ArmorCard, self).__repr__(),
            self.get_armor_type_string())


CreatureTypes = enum("Invalid", "Human", "Animal", "MagicBeing", "ShadowBeing", "LightBeing")


class CreatureCard(Card):
    def __init__(self, *args, **kwargs):
        super(CreatureCard, self).__init__(*args, **kwargs)

    def get_creature_type_string(self):
        creature_types = CreatureTypes.__dict__
        return str(list(creature_types)[creature_types.values().index(self.creature_type)])

    def initialize_card(self, *args, **kwargs):
        super(CreatureCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Creature
        self.creature_type = CreatureTypes.__dict__[
            kwargs["creature_type"]] if "creature_type" in kwargs else CreatureTypes.Invalid

    def __repr__(self):
        return "{0}\nCreature Type: {1}".format(
            super(CreatureCard, self).__repr__(),
            self.get_creature_type_string())


MagicTypes = enum("Invalid", "Physical", "Magical")


class MagicCard(Card):
    def __init__(self, *args, **kwargs):
        super(MagicCard, self).__init__(*args, **kwargs)

    def get_magic_type_string(self):
        magic_types = MagicTypes.__dict__
        return str(list(magic_types)[magic_types.values().index(self.magic_type)])

    def initialize_card(self, *args, **kwargs):
        super(MagicCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Magic
        self.magic_type = MagicTypes.__dict__[kwargs["magic_type"]] if "magic_type" in kwargs else MagicTypes.Invalid

    def __repr__(self):
        return "{0}\nMagic Type: {1}".format(
            super(MagicCard, self).__repr__(),
            self.get_magic_type_string())


TrapTypes = enum("Invalid", "Player", "Enemy")


class TrapCard(Card):
    def __init__(self, *args, **kwargs):
        super(TrapCard, self).__init__(*args, **kwargs)

    def get_trap_type_string(self):
        trap_types = TrapTypes.__dict__
        return str(list(trap_types)[trap_types.values().index(self.trap_type)])

    def initialize_card(self, *args, **kwargs):
        super(TrapCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Trap
        self.trap_type = TrapTypes.__dict__[kwargs["trap_type"]] if "trap_type" in kwargs else TrapTypes.Invalid

    def __repr__(self):
        return "{0}\nTrap Type: {1}".format(
            super(TrapCard, self).__repr__(),
            self.get_trap_type_string())


WeaponTypes = enum("Invalid", "Blade", "Axe", "MagicPole")


class WeaponCard(Card):
    def __init__(self, *args, **kwargs):
        super(WeaponCard, self).__init__(*args, **kwargs)

    def get_weapon_type_string(self):
        weapon_types = WeaponTypes.__dict__
        return str(list(weapon_types)[weapon_types.values().index(self.weapon_type)])

    def initialize_card(self, *args, **kwargs):
        super(WeaponCard, self).initialize_card(*args, **kwargs)

        self.card_type = CardTypes.Weapon
        self.weapon_type = WeaponTypes.__dict__[
            kwargs["weapon_type"]] if "weapon_type" in kwargs else WeaponTypes.Invalid

    def __repr__(self):
        return "{0}\nWeapon Type: {1}".format(
            super(WeaponCard, self).__repr__(),
            self.get_weapon_type_string())
