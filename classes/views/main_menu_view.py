import pygame
from views.view import View

class MainMenuView(View):
    def __init__(self):
        self._model = None

    def enter(self, event_dispatcher):
        pass

    def render(self, surface):
        surface.fill((0,0,0))

        title = self._model.title.render("Land: Duels", True, (255, 255, 255))
        surface.blit(title, (400 - title.get_width() // 2, 100 - title.get_height() // 2))

        self._model.menu.draw(surface)

        pygame.display.flip()

    def exit(self):
        pass

    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    model = property(get_model, set_model)