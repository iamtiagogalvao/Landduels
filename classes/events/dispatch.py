import logging

module_logger= logging.getLogger('landduels.dispatch')
module_logger.setLevel(logging.DEBUG)

import weakref


class EventDispatcher(object):
    def __init__(self):
        self._subscribers = weakref.WeakKeyDictionary()

    def subscribe_to_event(self, event_class, subscriber):
        entry= EventDispatcherEntry(self, event_class, subscriber)
        self._subscribers.setdefault(event_class, []).append(weakref.ref(entry))
        return entry

    def unsubscribe_from_event(self, event_class, subscriber):
        try:
            self._subscribers[event_class].remove(weakref.ref(subscriber))
        except KeyError:
            pass

    def dispatch_event(self, event):
        try:
            for entry in self._subscribers[event.__class__]:
                if entry():
                    entry()._subscriber(event)
                else:
                    self._subscribers[event.__class__].remove(entry)
        except KeyError:
            pass

class EventDispatcherEntry(object):
    def __init__(self, dispatcher, event, subscriber):
            self._dispatcher= dispatcher
            self._lookup= event
            self._subscriber= subscriber