import pygame
import ConfigParser
from events.eventlog import logger
from events.event import PyGameEventProcessor
from events.event import QuitEvent
from events.command import Command

from models.main_menu_model import MainMenuModel
from views.main_menu_view import MainMenuView
from controllers.main_menu_controller import MainMenuController


class Game(object):
    def __init__(self):
        self.display_surf = None
        self.clock = None

        self.config = ConfigParser.ConfigParser()
        self.config.read("landduels.ini")

        self.model = None
        self.view = None
        self.controller = None

        self.event_processor = PyGameEventProcessor()
        self.event_dispatcher = self.event_processor.get_dispatcher()

        self._connections = [
            self.event_dispatcher.subscribe_to_event(QuitEvent, Command(self.exit))
        ]
        self.is_running = True

    def init(self):
        pygame.init()
        width = int(self.config.get("Graphics", "Width"))
        height = int(self.config.get("Graphics", "Height"))
        self.display_surf = pygame.display.set_mode((width, height), pygame.HWSURFACE)

        self.set_mvc(MainMenuModel(), MainMenuView(), MainMenuController())

        self.clock = pygame.time.Clock()
        return True

    def exit(self, event):
        logger.info('Game: Shutting down the game client...')
        self.is_running = False

    def run(self):
        while self.is_running:
            self.clock.tick(60)
            dt = self.clock.get_time() / 1000.0
            self.event_processor.process_events()
            self.controller.update(dt)
            self.view.render(self.display_surf)
        pygame.quit()

    def set_mvc(self, model, view, controller):
        if self.model:
            self.model.exit()
        self.model = model
        self.model.enter(self.event_dispatcher)

        if self.view:
            self.view.exit()
        self.view = view
        self.view.enter(self.event_dispatcher)

        if self.controller:
            self.controller.exit()
        self.controller = controller
        self.controller.set_app(self)
        self.controller.set_model(self.model)
        self.controller.set_view(self.view)
        self.controller.enter(self.event_dispatcher)


if __name__ == "__main__":
    logger.info('Game: Starting up the game client...')
    logger.info('Game: Calling Game.init()...')

    game = Game()
    if game.init():
        game.run()

