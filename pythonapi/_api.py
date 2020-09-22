class API:
    def __init__(self, data):
        self.data = self.adapt(data)

    def adapt(self, data):
        return data


class Request(API):
    pass

class Response(API):
    pass