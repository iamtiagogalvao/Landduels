from abc import ABCMeta, abstractmethod, abstractproperty

class Controller(object):
    '''
    Controller handles events and updates the model.
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def enter(self, event_dispatcher):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def exit(self):
        pass

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    model = abstractproperty(get_model, set_model)

    def get_app(self):
        return self.app

    def set_app(self, app):
        self.app = app

    app = abstractproperty(get_app, set_app)