from pythonapi.domain.line import Line

class Paragraph:
    def __init__(self, paragraph: [str]):
        self.paragraph = [Line(line, paragraph) for line in paragraph]

    def __len__(self):
        return len(self.paragraph)

    def __getitem__(self, i):
        return self.paragraph[i]

    def index(self, item: Line) -> int:
        return self.paragraph.index(item)

    def sort(self):
        i = 0
        line = self[i]
        for line in self.paragraph:
            while not line.in_good_position():
                line.move_back()
        
    def to_dict(self):
        pass