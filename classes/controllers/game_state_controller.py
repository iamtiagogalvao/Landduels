from events.event import QuitEvent
from events.command import Command

class GameStateController:
    def __init__(self, event_processor):
        self._dispatcher= event_processor.get_dispatcher()
        self._connections= [
            self._dispatcher.subscribe_to_event(QuitEvent, Command(self.on_quit_game))
        ]

        self._running= True

    def on_quit_game(self, event):
        self._running= False
        print "Quit event received..."

    def is_running(self):
        return self._running