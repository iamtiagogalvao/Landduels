import logging

module_logger= logging.getLogger('landduels.main_menu_model')
module_logger.setLevel(logging.DEBUG)

import pygame
from models.model import Model


class MainMenuModel(Model):
    def __init__(self):
        pass

    def enter(self, event_dispatcher):
        pass

    def exit(self):
        pass

