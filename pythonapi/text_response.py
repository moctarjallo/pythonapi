from ._api import Response

class TextResponse(Response):

    def adapt(self, data:{}):
        form = '\n'
        form += self.format(data, 0)
        return form

    def format(self, data: {}, i):
        res = ''
        for k, v in data.items():
            res += '    '*i
            if not isinstance(v, dict):
                res += f"{k.upper()}: {str(v).capitalize()}\n"
            else:
                res += f"{k.upper()}:\n"
                res += self.format(v, i+1)
        return res