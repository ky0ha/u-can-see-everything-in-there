from inspect import getfullargspec

class Function(object):
    def __init__(self, fn):
        self.fn = fn
    
    def __call__(self, *args, **kwargs):
        fn = Namespace.get_instance().get(self.fn, *args)
        if not fn:
            raise Exception("no matching function found.")
        return fn(*args, **kwargs)
    
    def key(self, argspec=None):
        if argspec is None:
            argspec = getfullargspec(self.fn)
        return tuple([
            self.fn.__module__,
            self.fn.__class__,
            self.fn.__name__,
            tuple(str(arg) for arg in argspec),
        ])

class Namespace(object):
    __instance = None
    
    def __init__(self):
        if self.__instance is None:
            self.function_map = dict()
            Namespace.__instance = self
        else:
            raise Exception("cannot instantiate Namespace again.")
    
    @staticmethod
    def get_instance():
        if Namespace.__instance is None:
            Namespace()
        return Namespace.__instance
    
    def register(self, fn):
        func = Function(fn)
        # specs = getfullargspec(fn)
        # print(func.key())
        self.function_map[func.key()] = fn
        return func
    
    def get(self, fn, *args):
        func = Function(fn)
        print(self.function_map, end='\n\n')
        print(func.key(argspec=args))
        return self.function_map.get(func.key(argspec=args))

def overload(fn):
    return Namespace.get_instance().register(fn)