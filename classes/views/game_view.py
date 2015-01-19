import pygame
from views.view import View

class GameView(View):
    def __init__(self):
        self._model = None
        self.dispatcher = None
        self.connections = []

    def enter(self, event_dispatcher):
        self.dispatcher = event_dispatcher

    def render(self, surface):
        surface.fill((0,0,0))

        title = self._model.title.render("Game View", True, (255, 255, 255))
        surface.blit(title, (330, 100))

        pygame.display.flip()

    def exit(self):
        self.dispatcher = None
        self.connections = []

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    model = property(get_model, set_model)