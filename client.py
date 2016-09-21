import pygame
import ConfigParser
from events.eventlog import logger
from events.dispatch import EventDispatcher
from events.event import QuitEvent
from events.event import TickEvent
from events.command import Command
from events.event import MVCChangeEvent
from controllers.tick_controller import TickController
from models.main_menu_model import MainMenuModel
from views.main_menu_view import MainMenuView
from controllers.main_menu_controller import MainMenuController
from controllers.mouse_controller import MouseController


class GameClient(object):
    def __init__(self, event_dispatcher):
        self.display_surf = None
        self.config = ConfigParser.ConfigParser()
        self.config.read("landduels.ini")
        self.event_dispatcher = event_dispatcher

        self._connections = [
            self.event_dispatcher.subscribe_to_event(TickEvent, Command(self.update)),
            self.event_dispatcher.subscribe_to_event(QuitEvent, Command(self.exit)),
            self.event_dispatcher.subscribe_to_event(MVCChangeEvent, Command(self.mvc_change))
        ]

        pygame.init()
        width = int(self.config.get("Graphics", "Width"))
        height = int(self.config.get("Graphics", "Height"))
        self.display_surf = pygame.display.set_mode((width, height), pygame.HWSURFACE)

        self.model = MainMenuModel(event_dispatcher)
        self.view = MainMenuView(self.display_surf, event_dispatcher)
        self.controller = []
        self.controller.append(MouseController(event_dispatcher))
        self.controller.append(MainMenuController(self.view, event_dispatcher))

    def mvc_change(self, event):
        self.model.dispose(event)
        self.model = event.model

        self.view.dispose(event)
        self.view = event.view
        self.view.set_surface(self.display_surf)

        for controller in self.controller:
            controller.dispose(event)
        self.controller = event.controller

    def exit(self, event):
        pygame.quit()

    def update(self, dt):
        pass


if __name__ == "__main__":
    logger.info('Game: Starting up the game client...')

    dispatcher = EventDispatcher()
    tick_controller = TickController(dispatcher)
    game = GameClient(dispatcher)
    tick_controller.update()
