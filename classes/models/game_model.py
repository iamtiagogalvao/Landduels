import pygame
from pygame.sprite import Group
from models.model import Model
from cards.deck import Deck

class GameModel(Model):
    def __init__(self):
        self.dispatcher = None
        self.connections = []
        self.deck = Deck('classes/decks/starterdeck.json')
        self.deck.cards[0].scale(0.8)
        self.deck.cards[0].position(300, 420)
        self.deck.cards[1].scale(0.8)
        self.deck.cards[1].position(1000, 420)
        self.cards = Group(self.deck.cards)

    def enter(self, event_dispatcher):
        self.dispatcher = event_dispatcher

    def exit(self):
        self.dispatcher = None
        self.connections = []