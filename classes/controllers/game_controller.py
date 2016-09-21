from events.event import TickEvent
from events.event import QuitEvent
from events.command import Command


class GameController(object):
    def __init__(self, model, event_dispatcher):
        self._model = model
        self.angle = 0
        self.event_dispatcher = event_dispatcher
        self.connections = [
            self.event_dispatcher.subscribe_to_event(TickEvent, Command(self.update)),
            self.event_dispatcher.subscribe_to_event(QuitEvent, Command(self.dispose))
        ]

    def update(self, dt):
        self.angle += 0.1
        self.angle %= 360
        self._model.deck.cards[0].rotate(-self.angle)
        self._model.deck.cards[1].rotate(self.angle)

    def dispose(self, event):
        self.event_dispatcher = None
        self.connections = []
