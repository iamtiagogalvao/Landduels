from abc import ABCMeta, abstractmethod

class Model(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def enter(self, event_dispatcher):
        pass

    @abstractmethod
    def exit(self):
        pass
