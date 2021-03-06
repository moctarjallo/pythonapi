import unittest

from pythonapi.domain import Paragraph, Line

class TestIndex(unittest.TestCase):
    def test_index(self):
        parag = Paragraph(['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n'])
        line = Line('        C: Cc\n', parag.lines)
        line_index = parag.index(line)
        self.assertEqual(line_index, 2)

        line = Line('    B: Bb\n', parag.lines)
        line_index = parag.index(line)
        self.assertEqual(line_index, 4)

class TestGetItem(unittest.TestCase):
    def test_getitem(self):
        parag = Paragraph(['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n'])
        line = parag[2]
        self.assertEqual(line, Line('        C: Cc\n', parag.lines))        
        line = parag[4]
        self.assertEqual(line, Line('    B: Bb\n', parag.lines))

class TestEqual(unittest.TestCase):
    def test_equal_simple(self):
        parag1 = Paragraph(['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n'])
        parag2 = Paragraph(['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n'])
        self.assertEqual(parag1, parag2)

    def test_not_equal_simple(self):
        parag1 = Paragraph(['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n'])
        parag2 = Paragraph(['A:\n', '       E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n'])
        self.assertNotEqual(parag1, parag2)  

    def test_slice(self):
        parag = Paragraph(['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n'])
        sub_parag = parag[1:3]
        self.assertEqual(sub_parag,
            Paragraph(['    E:\n', '        C: Cc\n'])
        )

class TestSort(unittest.TestCase):
    def test_sort(self):
        parag = Paragraph(['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n'])
        parag.sort()
        self.assertEqual(parag, 
            Paragraph(['A:\n', '    B: Bb\n', '    E:\n', '        D: Dd\n', '        C: Cc\n'])
        )

    def test_sort_3levels(self):
        parag = Paragraph(['A:\n', '    E:\n', '        C: Cc\n'])
        parag.sort()
        self.assertEqual(parag,
            Paragraph(['A:\n', '    E:\n', '        C: Cc\n'])
        )

    def test_sort_2levels(self):
        parag = Paragraph(['A:\n', 'B:\n', '      C: Cc\n'])
        # print(f"parag before sort:\n{parag.lines}")
        parag.sort()
        # print(f"parag after sort:\n{parag.lines}")
        self.assertEqual(parag, 
            Paragraph(['A:\n', 'B:\n', '      C: Cc\n'])
        )


if __name__ == '__main__':
    unittest.main()