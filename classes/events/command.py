import weakref

class Command:
    def __init__(self, method):
        self._self = weakref.ref(method.__self__)
        self._func = method.__func__

    def __call__(self, *args, **kwargs):
        _self = self._self()
        if _self is None:
            raise weakref.ReferenceError()
        return self._func(_self, *args, **kwargs)

    def is_valid(self):
        return self._self() is not None
