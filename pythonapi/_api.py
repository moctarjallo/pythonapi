class API:
    def __init__(self, *args, **kwargs):
        self.data = self.adapt(*args, **kwargs)

    def adapt(self, *args, **kwargs):
        return args[0]


class Request(API):
    pass

class Response(API):
    pass