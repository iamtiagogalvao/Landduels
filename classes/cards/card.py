'''##########################################################
   # Card CLASS -> This is the main class for cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

import pygame
import uuid
from pygame.sprite import Sprite
from util.enum import enum

CardTypes = enum("Invalid", "Creature", "Magic", "Trap", "Action", "Armor", "Weapon")

class Card(Sprite):

    def __init__(self, *args, **kwargs):
        super(Card, self).__init__()
        self.initialize_card(*args, **kwargs)

    def scale(self, factor):
        self._scale = factor
        self.image = self._image.copy()
        self.image = pygame.transform.rotozoom(self.image, self._angle, factor)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def rotate(self, angle):
        self._angle = angle
        self.image = self._image.copy()
        self.image = pygame.transform.rotozoom(self.image, angle, self._scale)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def position(self, x, y):
        self.x = x
        self.y = y
        self.rect.center= (self.x, self.y)

    def initialize_card(self, *args, **kwargs):
        self.card_id = uuid.uuid1()
        self.card_type = kwargs["card_type"] if "card_type" in kwargs else CardTypes.Invalid
        self.mana_cost = kwargs["mana_cost"] if "mana_cost" in kwargs else 0
        self.image_path = kwargs["image"] if "image" in kwargs else "res/img/wiseman.png"
        self._image = pygame.image.load(self.image_path).convert()
        self.name = kwargs["name"] if "name" in kwargs else "Unnamed"
        self.attack = kwargs["attack"] if "attack" in kwargs else 0
        self.defense = kwargs["defense"] if "defense" in kwargs else 0

        # remaining defaults.
        self.image = self._image.copy()
        self.rect = self.image.get_rect()
        self._scale = 1.0
        self._angle = 0.0
        self.y = 0
        self.x = 0

    def __repr__(self):
        card_types= CardTypes.__dict__
        return "Card Name: {0}\nCard ID: {1}\nCard Image: {2}\nCard Type: {3}\nAttack: {4}\nDefense: {5}\nMana Cost: {6}".format(
            self.name,
            self.card_id,
            self.image_path,
            list(card_types)[card_types.values().index(self.card_type)],
            self.attack,
            self.defense,
            self.mana_cost)

