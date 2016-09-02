import pygame
from views.view import View

class GameView(View):
    def __init__(self, model):
        self.dispatcher = None
        self.connections = []
        self._model = model
        self.basic_font = "res/fonts/basic_bold.ttf"
        self.title = pygame.font.Font(self.basic_font, 24)

    def enter(self, event_dispatcher):
        self.dispatcher = event_dispatcher

    def render(self, surface):
        surface.fill((32,32,32))

        title_surface = self.title.render("Game View", True, (255, 255, 255))
        surface.blit(title_surface, (580, 40))

        self._model.cards.draw(surface)

        pygame.display.flip()

    def exit(self):
        self.dispatcher = None
        self.connections = []

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    model = property(get_model, set_model)