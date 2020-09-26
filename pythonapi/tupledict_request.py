from ._api import Request

class TupleDictRequest(Request):

    def adapt(self, *args:([{}]), **kwargs):
        data = args[0]
        res = {}
        for d in data:
            k, v = list(d.items())[0]
            if isinstance(v, tuple):
                v = self.adapt(v)
            res.update({k:v})
        return res