

class Model(object):
    def __init__(self, event_dispatcher):
        self._dispatcher = event_dispatcher
        self._connections = []
