from pythonapi._api import Request

from pythonapi.domain import Line, Paragraph

def get_paragraphs(text:[str]) -> [[str]]:
    parags = []
    try:
        parag_index = text.index('\n')
    except ValueError:
        return parags
    parag = text[:parag_index]
    parags.append(parag)
    parags += get_paragraphs(text[parag_index+1:])
    parags = list(filter(lambda line: line != [], parags))
    return parags


class TextRequest(Request):
    def adapt(self, *args:([str], ...), **kwargs):
        text:[[str]] = get_paragraphs(args[0])
        text = [Paragraph(paragraph) for paragraph in text]
        for paragraph in text:
            paragraph.sort()
        return [self.process(paragraph) for paragraph in text]

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