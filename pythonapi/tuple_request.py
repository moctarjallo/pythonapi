from ._api import Request

class TupleRequest(Request):

    def adapt(self, inputs: tuple):
        d = {}
        d['firstname'] = inputs[0]
        d['lastname'] = inputs[1]
        d['address'] = inputs[2]
        d['balance'] = int(inputs[3])
        return d