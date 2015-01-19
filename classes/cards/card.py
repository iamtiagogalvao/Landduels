'''##########################################################
   # Card CLASS -> This is the main class for cards
   # Created: 2015 - 01 - 09
   # Slaveworx, (add your credits here joe)
   #########################################################'''

import pygame
from pygame.sprite import Sprite

class Card(Sprite):

    def __init__(self, image):
        super(Card, self).__init__()
        self._image = self.card_image(image)
        self.image = self._image.copy()
        self.rect = self.image.get_rect()
        self._scale = 1.0
        self._angle = 0.0
        self.y = 0
        self.x = 0

    card_types = ("creature", "magic", "trap", "action", "armor", "weapon")

    def atack(self, atack):
        return int(atack)

    def defense(self, defense):
        return int(defense)

    def name(self, name):
        return str(name)

    def card_image(self, path):
        self.image = pygame.image.load(path).convert_alpha()
        return self.image

    def mana_cost(self, cost):
        return int(cost)

    def card_type(self, card_type):
        if card_type not in self.card_types:
           print "the card type is not known"
        return str(card_type)

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

