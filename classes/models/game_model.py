import pygame
from pygame.sprite import Group
from models.model import Model
from cards.deck import Deck

class GameModel(Model):
    def __init__(self):
        self.dispatcher = None
        self.connections = []
        self.basic_font = "res/fonts/basic_bold.ttf"
        self.title = pygame.font.Font(self.basic_font, 24)
        self.deck = Deck('classes/decks/starterdeck.json')
        self.deck.cards[0].scale(0.6)
        self.deck.cards[0].position(410, 420)
        self.deck.cards[1].scale(0.6)
        self.deck.cards[1].position(850, 420)
        self.cards = Group(self.deck.cards)

    def enter(self, event_dispatcher):
        self.dispatcher = event_dispatcher

    def exit(self):
        self.dispatcher = None
        self.connections = []