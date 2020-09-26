from ._api import Request

class TupleRequest(Request):

    def adapt(self, *args, **kwargs):
        keys, values = args[0], args[1]
        return dict(zip(keys, values))