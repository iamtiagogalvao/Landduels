import logging
import weakref

module_logger= logging.getLogger('landduels.main_menu_model')
module_logger.setLevel(logging.DEBUG)

import pygame
from models.model import Model
from events.event import MouseEnteredButtonEvent, MouseLeftButtonEvent
from events.command import Command
from util.enum import ButtonStates

class MainMenuModel(Model):

    def __init__(self, event_dispatcher):
        super(MainMenuModel, self).__init__(event_dispatcher)

        self._connections = [
            self._dispatcher.subscribe_to_event(MouseEnteredButtonEvent, Command(self.on_mouse_enter_button)),
            self._dispatcher.subscribe_to_event(MouseLeftButtonEvent, Command(self.on_mouse_leave_button))
        ]

        self.title_font = "res/fonts/title.ttf"
        self.basic_font = "res/fonts/basic.ttf"
        self.title = pygame.font.Font(self.title_font, 200)

        self.play_button = {}
        self.play_button["id"] = "play"
        self.play_button["image"] = pygame.image.load("res/img/play.png").convert_alpha()
        self.play_button["image"].get_rect(center=(300,300))
        self.play_button["state"] = ButtonStates.NORMAL
        self.play_button["scale"] = 1

        self.buttons = {}
        self.buttons[self.play_button["id"]]= self.play_button

    def on_mouse_enter_button(self, event):
        button = self.buttons[event.button["id"]]
        button["state"] = ButtonStates.MOUSEOVER
        button["scale"] = 1.05
        module_logger.info("MainMenuModel: Mouse enter button event: {0}".format(event.button))

    def on_mouse_leave_button(self, event):
        button = self.buttons[event.button["id"]]
        button["state"] = ButtonStates.NORMAL
        button["scale"] = 1
        module_logger.info("MainMenuModel: Mouse leave button event: {0}".format(event.button))
