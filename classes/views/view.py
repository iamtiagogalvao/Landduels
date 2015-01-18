from abc import ABCMeta, abstractmethod, abstractproperty

class View(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def enter(self, event_dispatcher):
        pass

    @abstractmethod
    def render(self, surface):
        pass

    @abstractmethod
    def exit(self):
        pass

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    model = abstractproperty(get_model, set_model)

