from ._api import Request

class TupleRequest(Request):

    def adapt(self, *args:((())), **kwargs):
        data = args[0]
        res = {}
        for t in data:
            k, v = t
            if isinstance(v, tuple):
                v = self.adapt(v)
            res.update({k:v})
        return res