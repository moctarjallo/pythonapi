from pythonapi.domain.line import Line

class Paragraph:
    def __init__(self, lines: [str]):
        self.lines = lines
        # self.paragraph = [Line(line, lines) for line in lines]

    def __eq__(self, other):
        return self.lines == other.lines

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, i):
        return Line(self.lines[i], self.lines)

    def index(self, item: Line) -> int:
        return self.lines.index(item.line)

    def sort(self):
        # i = 0
        # line = self.paragraph[i]
        paragraph = [Line(line, self.lines) for line in self.lines]
        for line in paragraph:
            while not line.in_good_position():
                line.move_back()
        
    def to_dict(self):
        pass

if __name__ == '__main__':
    paragraph = ['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n']
    Paragraph(paragraph).sort()
    # line = Line('    B: Bb\n', paragraph)
    # print(line.in_good_position())

