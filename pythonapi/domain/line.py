
class Line:
    def __init__(self, line: str, paragraph: [str]):
        self.line = line
        self.paragraph = paragraph

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
        return self.line.count(' ')

    @property
    def index(self):
        return self.paragraph.index(self.line)

    def strip(self):
        return self.line.strip()

    def in_good_position(self):
        previous_line = Line(self.paragraph[self.index-1], self.paragraph)
        if self.spaces >= previous_line.spaces:
            return True
        else:
            return False

    def move_back(self):
        i = self.index
        temp = self.paragraph[i-1]
        self.paragraph[i-1] = self.paragraph[i]
        self.paragraph[i] = temp