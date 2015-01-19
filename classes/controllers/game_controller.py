from controllers.controller import Controller
import math

class GameController(Controller):
    def __init__(self):
        self._model = None
        self.dispatcher = None
        self.connections = []
        self.angle= 0

    def enter(self, event_dispatcher):
        self.dispatcher = event_dispatcher

    def update(self, dt):
        self.angle += 1
        self.angle = self.angle % 360
        self._model.card.rotate_card_image(self.angle)

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