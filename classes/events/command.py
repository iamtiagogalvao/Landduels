import weakref

class Command(object):
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

class UnboundCommand(object):
    def __init__(self, method, *args, **kwargs):
        self._self = weakref.ref(method)
        self._func = method
        self._args = args
        self._kwargs = kwargs

    def __call__(self):
        _self = self._self()
        _args = self._args
        _kwargs = self._kwargs
        if self is None:
            raise weakref.ReferenceError()
        return self._func(*_args, **_kwargs)
