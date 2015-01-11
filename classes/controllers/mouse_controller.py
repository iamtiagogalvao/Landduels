from events.command import Command
from events.event import MouseMoveEvent

class MouseController(object):
    def __init__(self, event_processor):
        self._dispatcher= event_processor.get_dispatcher()
        self._connections= [
            self._dispatcher.subscribe_to_event(MouseMoveEvent, Command(self.on_mouse_move))
        ]

    def on_mouse_move(self, event):
        print "Mouse move event: {0}".format(event.data.pos)

        # Testing unsubscribing from events
        if event.data.pos == (100, 100):
            #self._dispatcher.unsubscribe_from_event(MouseMoveEvent, self._connections[0])
            self._connections= []