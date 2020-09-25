from pythonapi._api import Request

from pythonapi.domain import Line, Paragraph

class TextRequest(Request):
    def adapt(self, paragraph: [str]):
        paragraph = Paragraph(paragraph)
        paragraph.sort()
        return self.process(paragraph)

    def process(self, paragraph:Paragraph):
        # paragraph.sort(key=lambda line: line.count(' '))
        res = {}
        i = 0
        while i < len(paragraph):
            line = paragraph[i]
            k, v = line.get_key_value()
            if v != '':
                res[k] = v
                i+=1
            else:
                i+=1
                paragraph = paragraph[i:]
                v = self.process(paragraph)
                res[k] = v
                i+=len(paragraph)
        return res

if __name__ == '__main__':
    paragraph = ['CLIENT:\n', '    FIRSTNAME: Moctar\n']
    request = TextRequest(paragraph)
    print(request.data)