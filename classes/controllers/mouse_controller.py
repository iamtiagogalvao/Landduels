from events.event import MouseButtonDownEvent
from events.event import MouseButtonUpEvent
from events.event import MouseMoveEvent
from events.event import TickEvent
from events.event import QuitEvent
from events.command import Command
import pygame


event_lookup = {
    pygame.MOUSEMOTION: MouseMoveEvent,
    pygame.MOUSEBUTTONDOWN: MouseButtonDownEvent,
    pygame.MOUSEBUTTONUP: MouseButtonUpEvent,
    pygame.QUIT: QuitEvent,
}


class MouseController(object):
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher
        self.connections = [
            self.event_dispatcher.subscribe_to_event(TickEvent, Command(self.update))
        ]

    def update(self, dt):
        for pygame_event in pygame.event.get():
            if pygame_event.type in event_lookup.keys():
                self.event_dispatcher.dispatch_event(event_lookup[pygame_event.type](pygame_event))

    def dispose(self, event):
        self.event_dispatcher = None
        self.connections = []
