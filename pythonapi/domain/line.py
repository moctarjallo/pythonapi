
class Line:
    def __init__(self, line: str, paragraph: [str]):
        self.line = line
        self.paragraph = paragraph

    def __eq__(self, other):
        return self.line == other.line and self.paragraph == other.paragraph

    def get_key_value(self):
        k, v = self.line.strip().split(':')
        k = k.lower()
        v = v.strip()
        try:
            v = f"{v[0].lower()}{v[1:]}"
        except IndexError:
            v = ''
        return k, v

    @property
    def spaces(self):
        return self.line.split(':')[0].count(' ')

    @property
    def index(self):
        return self.paragraph.index(self.line)

    def strip(self):
        return self.line.strip()

    def in_good_position(self):
        previous_index = self.index - 1
        if previous_index < 0:
            return True
        previous_line = Line(self.paragraph[previous_index], self.paragraph)
        if self.spaces > previous_line.spaces:
            return True
        else:
            return False

    def move_back(self):
        i = self.index
        if i == 0:
            raise IndexError("Cannot move back before 1st index")
        else: # swap
            temp = self.paragraph[i-1]
            self.paragraph[i-1] = self.paragraph[i]
            self.paragraph[i] = temp

if __name__ == '__main__':
    # paragraph = Paragraph(['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n'])
    line_str = '    B: Bb\n'