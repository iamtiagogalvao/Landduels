import logging
from events.command import Command
from events.event import TickEvent

module_logger= logging.getLogger('landduels.main_menu_model')
module_logger.setLevel(logging.DEBUG)


class MainMenuModel(object):
    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher
        self.connections = [
            self.event_dispatcher.subscribe_to_event(TickEvent, Command(self.update))
        ]

    def update(self, dt):
        pass

    def dispose(self, event):
        self.event_dispatcher = None
        self.connections = []
