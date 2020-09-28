from ._api import Request

class TupleRequest(Request):

    def adapt(self, *args:((())), **kwargs):
        data = args[0]
        res = {}
        for t in data:
            if isinstance(t, dict):
                t = tuple(t.items())[0]
            k, v = t
            if isinstance(v, tuple): 
                v = self.adapt(v)
            else: # if v is a string number (int or float)
                try:
                    v = float(v)
                except Exception:
                    pass
            res.update({k:v})
        return res