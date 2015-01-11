from events.command import Command
from events.event import MouseMoveEvent

class MouseController:
    def __init__(self, event_processor):
        self._dispatcher= event_processor.get_dispatcher()
        self._connections= [
            self._dispatcher.subscribe_to_event(MouseMoveEvent, Command(self.on_mouse_move))
        ]

    def on_mouse_move(self, event):
        print "Mouse move event: {0}".format(event.data.pos)