
class EventDispatcher:
    def __init__(self):
        self._subscribers = {}

    def subscribe_to_event(self, event_class, subscriber):
        entry= EventDispatcherEntry(self, event_class, subscriber)
        self._subscribers.setdefault(event_class, []).append(entry)
        return entry

    def dispatch_event(self, event):
        try:
            for entry in self._subscribers[event.__class__]:
                entry._subscriber(event)
        except KeyError:
            pass

class EventDispatcherEntry:
    def __init__(self, dispatcher, event, subscriber):
            self._dispatcher= dispatcher
            self._lookup= event
            self._subscriber= subscriber