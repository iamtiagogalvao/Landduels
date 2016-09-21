import pygame
from pygame.sprite import Group
from cards.deck import Deck


class GameModel(object):
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher
        self.connections = []
        self.deck = Deck('classes/decks/starterdeck.json')
        self.deck.cards[0].scale(0.8)
        self.deck.cards[0].position(300, 420)
        self.deck.cards[1].scale(0.8)
        self.deck.cards[1].position(1000, 420)
        self.cards = Group(self.deck.cards)

    def dispose(self):
        self.event_dispatcher = None
        self.connections = []
