import pygame
from views.view import View

class MainMenuView(View):
    def __init__(self):
        self._model = None
        self._connections = []
        self._dispatcher = None

    def enter(self, event_dispatcher):
        self._dispatcher = event_dispatcher
        self._connections = [

        ]

    def render(self, surface):
        surface.fill((0,0,0))

        title = self._model.title.render("Land: Duels", True, (255, 255, 255))
        surface.blit(title, (380, 100))

        self._model.menu.draw(surface)

        pygame.display.flip()

    def exit(self):
        self._dispatcher = None
        self._connections = []
        self._model = None

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    model = property(get_model, set_model)