import pygame
import logging

logger= logging.getLogger('landduels')
logger.setLevel(logging.DEBUG)

file_handler= logging.FileHandler('game.events.log', mode='w')
file_handler.setLevel(logging.DEBUG)

console_handler= logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

log_formatter= logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(log_formatter)
console_handler.setFormatter(log_formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info('Game: Starting up the game...')

import ConfigParser
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
        self.controller= None

        self.event_processor = PyGameEventProcessor()
        self.event_dispatcher = self.event_processor.get_dispatcher()

        self._connections= [
            self.event_dispatcher.subscribe_to_event(QuitEvent, Command(self.exit))
        ]
        self.is_running = True

    def init(self):
        pygame.init()
        width= int(self.config.get("Graphics", "Width"))
        height= int(self.config.get("Graphics", "Height"))
        self.display_surf= pygame.display.set_mode((width, height), pygame.HWSURFACE)

        self.set_mvc(MainMenuModel(self.event_dispatcher), MainMenuView(), MainMenuController())

        self.clock = pygame.time.Clock()
        return True

    def exit(self, event):
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
        self.model = model

        if self.controller:
            self.controller.exit()
        self.controller = controller
        self.controller.set_model(self.model)
        self.controller.enter(self.event_dispatcher)

        if self.view:
            self.view.exit()
        self.view = view
        self.view.set_model(self.model)
        self.view.enter(self.event_dispatcher)


if __name__ == "__main__":
    game = Game()
    logger.info('Game: Calling Game::on_execute()...')
    if game.init():
        game.run()

