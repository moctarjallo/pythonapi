from ._api import Request

class TupleRequest(Request):

    def adapt(self, *args:((())), **kwargs):
        data = args[0]
        res = {}
        for t in data:
            k, v = t
            if isinstance(v, tuple): 
                v = self.adapt(v)
            elif isinstance(v, str) and v.isdigit():
                v = float(v)
            res.update({k:v})
        return res