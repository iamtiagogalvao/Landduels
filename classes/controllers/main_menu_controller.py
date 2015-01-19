import logging
import weakref

module_logger= logging.getLogger('landduels.main_menu_controller')
module_logger.setLevel(logging.DEBUG)

from controllers.controller import Controller
from events.event import MouseMoveEvent
from events.event import MouseEnteredButtonEvent, MouseLeftButtonEvent
from events.command import Command
from ui.button import ButtonState

class MainMenuController(Controller):

    def __init__(self):
        self._model = None
        self.dispatcher= None
        self.connections = []

    def enter(self, event_dispatcher):
        self.dispatcher = event_dispatcher
        self.connections = [
            self.dispatcher.subscribe_to_event(MouseMoveEvent, Command(self.on_mouse_move))
        ]

    def update(self, dt):
        pass

    def exit(self):
        self.connections = []

    def on_mouse_move(self, event):
        for button in self._model.buttons:
            if button.state == ButtonState.NORMAL:
                if self.mouse_is_over(button.rect, event.data.pos):
                    self.dispatcher.dispatch_event(MouseEnteredButtonEvent(button.id))
            if button.state == ButtonState.MOUSEOVER:
                if not self.mouse_is_over(button.rect, event.data.pos):
                    self.dispatcher.dispatch_event(MouseLeftButtonEvent(button.id))


    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    model = property(get_model, set_model)

    def mouse_is_over(self, rect, mouse_pos):
        return rect.collidepoint(mouse_pos)
