from controllers.controller import Controller

class GameController(Controller):
    def __init__(self):
        self._model = None
        self.dispatcher = None
        self.connections = []

    def enter(self, event_dispatcher):
        self.dispatcher = event_dispatcher

    def update(self, dt):
        pass

    def exit(self):
        self.dispatcher = None
        self.connections = []

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    model = property(get_model, set_model)

    def get_app(self):
        return self._app

    def set_app(self, app):
        self._app = app

    app = property(get_app, set_app)