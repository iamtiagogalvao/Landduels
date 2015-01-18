import logging
import weakref

module_logger= logging.getLogger('landduels.main_menu_controller')
module_logger.setLevel(logging.DEBUG)

from controllers.controller import Controller
from events.event import MouseMoveEvent
from events.event import MouseEnteredButtonEvent, MouseLeftButtonEvent
from events.command import Command
from util.enum import ButtonStates

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
        #module_logger.info("MainMenuController: Mouse move event: {0}".format(event.data.pos))

        play_button = self._model.play_button
        if play_button["state"] == ButtonStates.NORMAL:
            if self.mouse_is_over(play_button["image"].get_rect(), event.data.pos):
                self.dispatcher.dispatch_event(MouseEnteredButtonEvent(play_button))
        if play_button["state"] == ButtonStates.MOUSEOVER:
            if not self.mouse_is_over(play_button["image"].get_rect(), event.data.pos):
                self.dispatcher.dispatch_event(MouseLeftButtonEvent(play_button))

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    model = property(get_model, set_model)

    def mouse_is_over(self, rect, mouse_pos):
        return rect.collidepoint(mouse_pos)
