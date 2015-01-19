import logging

module_logger= logging.getLogger('landduels.ui.button')
module_logger.setLevel(logging.DEBUG)

import pygame
from pygame.sprite import Sprite
from events.event import MouseEnteredButtonEvent
from events.event import MouseLeftButtonEvent
from events.event import ButtonClickedEvent
from events.event import ButtonClickEndedEvent
from events.command import Command
from util.enum import enum

ButtonState = enum('NORMAL', 'MOUSEOVER', 'PRESSED')

class Button(Sprite):

    def __init__(self, id, imagepath, event_dispatcher, x, y):
        super(Button, self).__init__()

        self.dispatcher = event_dispatcher
        self._connections = [
            self.dispatcher.subscribe_to_event(MouseEnteredButtonEvent, Command(self.on_mouse_enter)),
            self.dispatcher.subscribe_to_event(MouseLeftButtonEvent, Command(self.on_mouse_leave)),
            self.dispatcher.subscribe_to_event(ButtonClickedEvent, Command(self.on_clicked)),
            self.dispatcher.subscribe_to_event(ButtonClickEndedEvent, Command(self.on_click_ended))
        ]

        self.id = id

        self.state = ButtonState.NORMAL

        self._image = pygame.image.load(imagepath).convert_alpha()
        self.image = self._image.copy()
        self.rect = self.image.get_rect()
        self.set_position(x, y)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def on_mouse_enter(self, event):
        if self.id == event.id:
            if self.state == ButtonState.NORMAL:
                self.state = ButtonState.MOUSEOVER
                module_logger.info("Button: on_mouse_enter was called in base button.")

    def on_mouse_leave(self, event):
        if self.id == event.id:
            if self.state == ButtonState.MOUSEOVER:
                self.state = ButtonState.NORMAL
                module_logger.info("Button: on_mouse_leave was called in base button.")

    def on_clicked(self, event):
        if self.id == event.id:
            if self.state == ButtonState.MOUSEOVER:
                self.state = ButtonState.PRESSED
                module_logger.info("Button: on_clicked was called in base button.")

    def on_click_ended(self, event):
        if self.id == event.id:
            if self.state == ButtonState.PRESSED:
                self.state = ButtonState.MOUSEOVER
                module_logger.info("Button: on_click_ended was called in base button.")