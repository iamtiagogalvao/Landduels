import pygame
from models.model import Model

class GameModel(Model):
    def __init__(self):
        self.dispatcher = None
        self.connections = []
        self.basic_font = "res/fonts/basic_bold.ttf"
        self.title = pygame.font.Font(self.basic_font, 24)

    def enter(self, event_dispatcher):
        self.dispatcher = event_dispatcher

    def exit(self):
        self.dispatcher = None
        self.connections = []