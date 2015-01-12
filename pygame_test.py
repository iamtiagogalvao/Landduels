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
from starterdeck import StarterDeck
from events.event import PyGameEventProcessor
from events.event import QuitEvent
from controllers.mouse_controller import MouseController
from controllers.game_state_controller import GameStateController

##### COLORS #####
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

deck = StarterDeck()

### TEXT CONFIGS ###
font_choice = {"title": "res/fonts/title.ttf", "basic": "res/fonts/basic.ttf", }


class Game(object):

    def __init__(self):
        self.display_surf = None
        self.clock = None
        self.last_time = 0
        self.config = ConfigParser.ConfigParser()
        self.config.read("landduels.ini")
        self.event_processor = PyGameEventProcessor()
        self.game_state_controller = GameStateController(self.event_processor)
        self.mouse_controller = MouseController(self.event_processor)
        self.font1= None
        self.font2= None
        self.title= None
        self.names= None
        self.play_button= None
        self.card_image= None

    def on_init(self):
        pygame.init()

        width = int(self.config.get("Graphics", "Width"))
        height = int(self.config.get("Graphics", "Height"))

        self.display_surf = pygame.display.set_mode((width, height), pygame.HWSURFACE)

        self.font1= pygame.font.Font(font_choice["title"], 200)
        self.title= self.font1.render("Land: Duels", True, (white))

        self.font2= pygame.font.Font(font_choice["basic"], 50)
        self.names= self.font2.render(deck.magic_cards["name"], True, (white))

        self.play_button= pygame.image.load("res/img/play.png")
        self.card_image= pygame.image.load(deck.magic_cards["image"])

        self.clock = pygame.time.Clock()

        return True

    def on_loop(self, dt):
        pass

    def on_render(self):
        self.display_surf.fill(black)
        self.display_surf.blit(self.title, (400 - self.title.get_width() // 2, 100 - self.title.get_height() // 2))
        self.display_surf.blit(self.play_button, (400 - self.play_button.get_width() // 2, 350 - self.play_button.get_height() // 2))
        self.display_surf.blit(self.names, (400 - self.names.get_width() // 2, 400 - self.names.get_height() // 2))
        self.display_surf.blit(self.card_image, (400 - self.card_image.get_width() // 2, 400 - self.card_image.get_height() // 2))
        pygame.display.flip()

    def on_exit(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.event_processor.get_dispatcher().dispatch_event(QuitEvent)

        while self.game_state_controller.is_running():
            self.clock.tick(60)
            dt = self.clock.get_time() / 1000.0
            self.event_processor.process_events()
            self.on_loop(dt)
            self.on_render()
        self.on_exit()


if __name__ == "__main__":
    game = Game()
    logger.info('Game: Calling Game::on_execute()...')
    game.on_execute()

