import logging

module_logger= logging.getLogger('landduels.main_menu_model')
module_logger.setLevel(logging.DEBUG)

import pygame
from pygame.sprite import Group
from models.model import Model
from events.event import GameStartedEvent
from ui.button import Button

class PlayButton(Button):
    def __init__(self, id, imagepath, event_dispatcher, x ,y):
        super(PlayButton, self).__init__(id, imagepath, event_dispatcher, x ,y)

    def on_mouse_enter(self, event):
        super(PlayButton, self).on_mouse_enter(event)
        module_logger.info("PlayButton: on_mouse_enter called in play button.")
        center = self.rect.center
        self.image = pygame.transform.rotozoom(self.image, 0.0, 1.05)
        self.rect = self.image.get_rect()
        self.rect.center = center

    def on_mouse_leave(self, event):
        super(PlayButton, self).on_mouse_leave(event)
        module_logger.info("PlayButton: on_mouse_leave called in play button.")
        center = self.rect.center
        self.image = self._image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = center

    def on_clicked(self, event):
        super(PlayButton, self).on_clicked(event)
        module_logger.info("PlayButton: on_clicked called in play button.")
        self.dispatcher.dispatch_event(GameStartedEvent(event))


class MainMenuModel(Model):
    def __init__(self):
        self.buttons = []
        self.menu = None
        self.title_font = "res/fonts/title.ttf"
        self.basic_font = "res/fonts/basic.ttf"
        self.title = pygame.font.Font(self.title_font, 200)

    def enter(self, event_dispatcher):
        self.buttons.append(PlayButton("play_button", "res/img/play.png", event_dispatcher, 480, 500))
        self.menu = Group(self.buttons)

    def exit(self):
        pass

