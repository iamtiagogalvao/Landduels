import pygame
from events.command import Command


class Event(object):
    def __init__(self, event):
        self.data = event


class TickEvent(Event):
    def __init__(self, dt):
        self.dt = dt


class QuitEvent(Event):
    pass


class MVCChangeEvent(Event):
    def __init__(self, model, view, controller):
        self.model = model
        self.view = view
        self.controller = controller


class MouseMoveEvent(Event):
    pass


class MouseEnteredButtonEvent(Event):
    def __init__(self, button_id):
        self.id = button_id


class MouseLeftButtonEvent(Event):
    def __init__(self, button_id):
        self.id = button_id


class ButtonClickedEvent(Event):
    def __init__(self, button_id):
        self.id = button_id


class ButtonClickEndedEvent(Event):
    def __init__(self, button_id):
        self.id = button_id


class MouseButtonDownEvent(Event):
    pass


class MouseButtonUpEvent(Event):
    pass


class GameStartedEvent(Event):
    pass

_event_lookup = {
    pygame.QUIT: QuitEvent,
    pygame.MOUSEMOTION: MouseMoveEvent,
    pygame.MOUSEBUTTONDOWN: MouseButtonDownEvent,
    pygame.MOUSEBUTTONUP: MouseButtonUpEvent
}


class EventProcessor(object):
    def __init__(self, event_dispatcher):
        self._event_queue = []
        self.dispatcher = event_dispatcher

    def process_events(self):
        for event in self._event_queue:
            self._dispatcher.dispatch_event(event)
        self._event_queue = []


class PyGameEventProcessor(EventProcessor):
    def __init__(self, event_dispatcher):
        super(PyGameEventProcessor, self).__init__(event_dispatcher)
        self._connections = [
            self.event_dispatcher.subscribe_to_event(TickEvent, Command(self.update))
        ]

    def update(self, dt):
        self.process_events()

    def process_events(self):
        for pygame_event in pygame.event.get():
            if pygame_event.type in _event_lookup.keys():
                self._event_queue.append(_event_lookup[pygame_event.type](pygame_event))
        super(PyGameEventProcessor, self).process_events()
