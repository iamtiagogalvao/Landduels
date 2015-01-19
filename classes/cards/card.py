'''##########################################################
   # Card CLASS -> This is the main class for cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

import pygame
from pygame.sprite import Sprite
from util.enum import enum

CardTypes = enum("Invalid", "Creature", "Magic", "Trap", "Action", "Armor", "Weapon")

class Card(Sprite):

    def __init__(self, *args, **kwargs):
        super(Card, self).__init__()
        self.initialize_card(*args, **kwargs)

    def scale_card_image(self, factor):
        self._scale = factor
        self.image = self._image.copy()
        self.image = pygame.transform.rotozoom(self.image, self._angle, factor)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def rotate_card_image(self, angle):
        self._angle = angle
        self.image = self._image.copy()
        self.image = pygame.transform.rotozoom(self.image, angle, self._scale)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def position_card_image(self, x, y):
        self.x = x
        self.y = y
        self.rect.center= (self.x, self.y)

    def initialize_card(self, *args, **kwargs):
        if kwargs.has_key("card_type"):
            self.card_type = kwargs["card_type"]
        else:
            self.card_type = CardTypes.Invalid

        if kwargs.has_key("mana_cost"):
            self.mana_cost = kwargs["mana_cost"]
        else:
            self.mana_cost = 0

        if kwargs.has_key("image"):
            self._image = pygame.image.load(kwargs["image"]).convert()
            self.image_path = kwargs["image"]
        else:
            self._image = pygame.image.load("res/img/wiseman.png").convert() # default
            self.image_path = "res/img/wiseman.png"

        if kwargs.has_key("name"):
            self.name = kwargs["name"]
        else:
            self.name = "Unnamed"

        if kwargs.has_key("attack"):
            self.attack = kwargs["attack"]
        else:
            self.attack = 0

        if kwargs.has_key("defense"):
            self.defense = kwargs["defense"]
        else:
            self.defense = 0

        # remaining defaults.
        self.image = self._image.copy()
        self.rect = self.image.get_rect()
        self._scale = 1.0
        self._angle = 0.0
        self.y = 0
        self.x = 0

    def __repr__(self):
        card_types= CardTypes.__dict__
        return "Card Name: {0}\nCard Image: {1}\nCard Type: {2}\nAttack: {3}\nDefense: {4}\nMana Cost: {5}".format(
            self.name,
            self.image_path,
            list(card_types)[card_types.values().index(self.card_type)],
            self.attack,
            self.defense,
            self.mana_cost)

