import pygame
from pygame.sprite import Group
from models.model import Model
from cards.actioncard import ActionCard

class GameModel(Model):
    def __init__(self):
        self.dispatcher = None
        self.connections = []
        self.basic_font = "res/fonts/basic_bold.ttf"
        self.title = pygame.font.Font(self.basic_font, 24)
        self.card = ActionCard(image="res/img/wiseman.png")
        self.card.scale_card_image(0.33)
        self.card.position_card_image(400, 310)
        self.cards = Group(self.card)

    def enter(self, event_dispatcher):
        self.dispatcher = event_dispatcher

    def exit(self):
        self.dispatcher = None
        self.connections = []