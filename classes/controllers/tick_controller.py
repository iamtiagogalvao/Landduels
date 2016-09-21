from events.event import QuitEvent
from events.event import TickEvent
from events.command import Command
import pygame


class TickController(object):
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.connections = [
            self.event_dispatcher.subscribe_to_event(QuitEvent, Command(self.dispose))
        ]

    def update(self):
        while self.is_running:
            self.clock.tick(60)
            dt = self.clock.get_time() / 1000.0
            tick = TickEvent(dt)
            self.event_dispatcher.dispatch_event(tick)

    def dispose(self, event):
        self.is_running = False
        self.event_dispatcher = None
        self.connections = []

