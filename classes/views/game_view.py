import pygame
from events.event import TickEvent
from events.event import QuitEvent
from events.command import Command


class GameView(object):
    def __init__(self, event_dispatcher):
        self.surface = None
        self.basic_font = "res/fonts/basic_bold.ttf"
        self.title = pygame.font.Font(self.basic_font, 24)
        self.event_dispatcher = event_dispatcher
        self.connections = [
            self.event_dispatcher.subscribe_to_event(TickEvent, Command(self.render)),
            self.event_dispatcher.subscribe_to_event(QuitEvent, Command(self.dispose))
        ]

    def set_surface(self, surface):
        self.surface = surface

    def render(self, dt):
        self.surface.fill((32, 32, 32))
        title_surface = self.title.render("Game View", True, (255, 255, 255))
        self.surface.blit(title_surface, (580, 40))
        pygame.display.flip()

    def dispose(self, event):
        self.event_dispatcher = None
        self.connections = []
