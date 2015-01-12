import logging

module_logger= logging.getLogger('landduels.game_state_controller')
module_logger.setLevel(logging.DEBUG)

from events.event import QuitEvent
from events.command import Command

class GameStateController(object):
    def __init__(self, event_processor):
        self._dispatcher= event_processor.get_dispatcher()
        self._connections= [
            self._dispatcher.subscribe_to_event(QuitEvent, Command(self.on_quit_game))
        ]

        self._running= True

    def on_quit_game(self, event):
        self._running= False
        module_logger.info("GameStateController: Quit event received...")

    def is_running(self):
        return self._running