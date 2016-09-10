import logging

module_logger = logging.getLogger('landduels.main_menu_controller')
module_logger.setLevel(logging.DEBUG)

from models.game_model import GameModel
from controllers.game_controller import GameController
from views.game_view import GameView

from controllers.controller import Controller
from events.event import MouseMoveEvent
from events.event import MouseEnteredButtonEvent
from events.event import MouseLeftButtonEvent
from events.event import MouseButtonDownEvent
from events.event import MouseButtonUpEvent
from events.event import ButtonClickedEvent
from events.event import ButtonClickEndedEvent
from events.event import GameStartedEvent
from events.command import Command
from ui.button import ButtonState

class MainMenuController(Controller):

    def __init__(self):
        self._app = None
        self.dispatcher= None
        self.connections = []

    def enter(self, event_dispatcher):
        self.dispatcher = event_dispatcher
        self.connections = [
            self.dispatcher.subscribe_to_event(MouseMoveEvent, Command(self.on_mouse_move)),
            self.dispatcher.subscribe_to_event(MouseButtonDownEvent, Command(self.on_mouse_button_down)),
            self.dispatcher.subscribe_to_event(MouseButtonUpEvent, Command(self.on_mouse_button_up)),
            self.dispatcher.subscribe_to_event(GameStartedEvent, Command(self.on_game_started))
        ]

    def update(self, dt):
        pass

    def exit(self):
        self._app = None
        self.dispatcher = None
        self.connections = []

    def on_mouse_move(self, event):
        for button in self._view.buttons:
            if button.state == ButtonState.NORMAL:
                if self.mouse_is_over(button.rect, event.data.pos):
                    self.dispatcher.dispatch_event(MouseEnteredButtonEvent(button.id))
            if button.state == ButtonState.MOUSEOVER:
                if not self.mouse_is_over(button.rect, event.data.pos):
                    self.dispatcher.dispatch_event(MouseLeftButtonEvent(button.id))

    def on_mouse_button_down(self, event):
        for button in self._view.buttons:
            if self.mouse_is_over(button.rect, event.data.pos):
                self.dispatcher.dispatch_event(ButtonClickedEvent(button.id))

    def on_mouse_button_up(self, event):
        for button in self._view.buttons:
            if self.mouse_is_over(button.rect, event.data.pos):
                self.dispatcher.dispatch_event(ButtonClickEndedEvent(button.id))

    def mouse_is_over(self, rect, mouse_pos):
        return rect.collidepoint(mouse_pos)

    def on_game_started(self, event):
        module_logger.info("MainMenuController: on_game_started called.")
        model = GameModel()
        view = GameView(model)
        controller = GameController()
        self._app.set_mvc(model, view, controller)

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    model = property(get_model, set_model)

    def get_view(self):
        return self._view

    def set_view(self, view):
        self._view = view

    view = property(get_view, set_view)

    def get_app(self):
        return self._app

    def set_app(self, app):
        self._app = app

    app = property(get_app, set_app)
