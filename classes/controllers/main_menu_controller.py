import logging
from models.game_model import GameModel
from controllers.game_controller import GameController
from controllers.mouse_controller import MouseController
from views.game_view import GameView
from events.event import TickEvent
from events.event import MouseMoveEvent
from events.event import MouseEnteredButtonEvent
from events.event import MouseLeftButtonEvent
from events.event import MouseButtonDownEvent
from events.event import MouseButtonUpEvent
from events.event import ButtonClickedEvent
from events.event import ButtonClickEndedEvent
from events.event import GameStartedEvent
from events.event import MVCChangeEvent
from events.command import Command
from ui.button import ButtonState

module_logger = logging.getLogger('landduels.main_menu_controller')
module_logger.setLevel(logging.DEBUG)


class MainMenuController(object):
    def __init__(self, view, event_dispatcher):
        self._view = view
        self.event_dispatcher = event_dispatcher
        self.connections = [
            self.event_dispatcher.subscribe_to_event(TickEvent, Command(self.update)),
            self.event_dispatcher.subscribe_to_event(MouseMoveEvent, Command(self.on_mouse_move)),
            self.event_dispatcher.subscribe_to_event(MouseButtonDownEvent, Command(self.on_mouse_button_down)),
            self.event_dispatcher.subscribe_to_event(MouseButtonUpEvent, Command(self.on_mouse_button_up)),
            self.event_dispatcher.subscribe_to_event(GameStartedEvent, Command(self.on_game_started))
        ]

    def update(self, dt):
        pass

    def dispose(self, event):
        self.event_dispatcher = None
        self.connections = []

    def on_mouse_move(self, event):
        for button in self._view.buttons:
            if button.state == ButtonState.NORMAL:
                if self.mouse_is_over(button.rect, event.data.pos):
                    self.event_dispatcher.dispatch_event(MouseEnteredButtonEvent(button.id))
            if button.state == ButtonState.MOUSEOVER:
                if not self.mouse_is_over(button.rect, event.data.pos):
                    self.event_dispatcher.dispatch_event(MouseLeftButtonEvent(button.id))

    def on_mouse_button_down(self, event):
        for button in self._view.buttons:
            if self.mouse_is_over(button.rect, event.data.pos):
                self.event_dispatcher.dispatch_event(ButtonClickedEvent(button.id))

    def on_mouse_button_up(self, event):
        for button in self._view.buttons:
            if self.mouse_is_over(button.rect, event.data.pos):
                self.event_dispatcher.dispatch_event(ButtonClickEndedEvent(button.id))

    def mouse_is_over(self, rect, mouse_pos):
        return rect.collidepoint(mouse_pos)

    def on_game_started(self, event):
        module_logger.info("MainMenuController: on_game_started called.")
        model = GameModel(self.event_dispatcher)
        view = GameView(self.event_dispatcher)
        controllers = []
        game_controller = GameController(model, self.event_dispatcher)
        mouse_controller = MouseController(self.event_dispatcher)
        controllers.append(game_controller)
        controllers.append(mouse_controller)
        event = MVCChangeEvent(model, view, controllers)
        self.event_dispatcher.dispatch_event(event)


