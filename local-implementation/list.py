# from inspect import getfullargspec

# class Function(object):
#     def __init__(self, fn):
#         self.fn = fn
    
#     def __call__(self, *args, **kwargs):
#         fn = Namespace.get_instance().get(self.fn, *args)
#         if not fn:
#             raise Exception("no matching function found")
#         return fn(*args, **kwargs)
    
#     def key(self, args=None):
#         if args is None:
#             args = getfullargspec(self.fn).args
#         return tuple([
#             self.fn.__module__,
#             self.fn.__class__,
#             self.fn.__name__,
#             len(args or []),
#         ])

# class Namespace(object):
#     __instance = None
    
#     def __init__(self):
#         if self.__instance is None:
#             self.function_map = dict()
#             Namespace.__instance = self
#         else:
#             raise Exception("cannot instantiate Namespace again")
    
#     @staticmethod
#     def get_instance():
#         if Namespace.__instance is None:
#             Namespace()
#         return Namespace.__instance

#     def register(self, fn):
#         func = Function(fn)
#         specs = getfullargspec(fn)
#         self.function_map[func.key()] = fn
#         return func

#     def get(self, fn, *args):
#         func = Function(fn)
#         return self.function_map.get(func.key(args=args))

def overload(fn):
    return Namespace.get_instance().register(fn)



from inspect import getfullargspec


class function(object):
    def __init__(self, fn):
        self.fn = fn
    
    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)
    
    def key(self, args=None, annotations=None):
        if args==None:
            args, annotations = getfullargspec(self.fn).args, getfullargspec(self.fn).annotations
        return tuple([
            self.fn.__module__,
            self.fn.__class__,
            self.fn.__name__,
            len(args or []),
            # args,
            # annotations,
        ])


class Namespace(object):
    __instance = None
    def __init__(self):
        if self.__instance is None:
            self.function_map = dict()
            Namespace.__instance = self
        else:
            raise Exception('cannot init Namespace again')
    
    @staticmethod
    def get_instance():
        if Namespace.__instance==None:
            Namespace()
        return Namespace.__instance

    def register(self, fn):
        func = function(fn)
        self.function_map[func.key()] = fn
        return func

    def get(self, fn, *args):
        func = function(fn)
        return Namespace.function_map[func.key(args=args)]

@overload
def num(a:int):
    print('int')
@overload
def num(a:str):
    print('str')

num(1)

