import unittest

from pythonapi.domain import Line

class TestEqual(unittest.TestCase):
    def setUp(self):
        self.paragraph = ['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n']

    def test_simple(self):
        line1 = Line('    B: Bb\n', self.paragraph)
        line2 = Line('    B: Bb\n', self.paragraph)
        self.assertEqual(line1, line2)

    def test_not_equal(self):
        line1 = Line('    B: Bb\n', self.paragraph)
        line2 = Line('      B: Bb\n', self.paragraph)
        self.assertNotEqual(line1, line2)

    def test_not_equal_different_paragraph(self):
        line1 = Line('    B: Bb\n', self.paragraph)
        line2 = Line('    B: Bb\n', self.paragraph+['A:\n'])
        self.assertNotEqual(line1, line2)

class TestGetKeyValue(unittest.TestCase):
    def setUp(self):
        self.paragraph = ['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n']

    def test_get_key_value(self):
        line = Line('    B: Bb\n', self.paragraph)
        k, v = line.get_key_value()
        self.assertEqual(k, 'b')
        self.assertEqual(v, 'bb')

    def test_get_key_empty_value(self):
        line = Line('A:\n', self.paragraph)
        k, v = line.get_key_value()
        self.assertEqual(k, 'a')
        self.assertEqual(v, '')

class TestSpaces(unittest.TestCase):
    def setUp(self):
        self.paragraph = ['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n']

    def test_spaces(self):
        line = Line('A:\n', self.paragraph)
        self.assertEqual(line.spaces, 0)

    def test_spaces_not_null(self):
        line = Line('    B: Bb\n', self.paragraph)
        self.assertEqual(line.spaces, 4)

        line = Line('        B: Bb\n', self.paragraph)
        self.assertEqual(line.spaces, 8)

class TestIndex(unittest.TestCase):
    def setUp(self):
        self.paragraph = ['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n']

    def test_index_simple(self):
        line = Line('    B: Bb\n', self.paragraph)
        self.assertEqual(line.index, 4)

        line = Line('        C: Cc\n', self.paragraph)
        self.assertEqual(line.index, 2)

class TestInGoodPosition(unittest.TestCase):
    def setUp(self):
        self.paragraph = ['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n']

    def test_in_good_position(self):
        line = Line('        C: Cc\n', self.paragraph)
        self.assertTrue(line.in_good_position())

    def test_in_bad_position(self):
        line = Line('    B: Bb\n', self.paragraph)
        self.assertFalse(line.in_good_position())

    def test_in_good_position_1st_element(self):
        line = Line('A:\n', self.paragraph)
        self.assertTrue(line.in_good_position())

class TestMoveBack(unittest.TestCase):

    def test_simple(self):
        paragraph = ['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n']
        line = Line('    B: Bb\n', paragraph)
        line.move_back()
        self.assertEqual(paragraph, 
            ['A:\n', '    E:\n', '        C: Cc\n', '    B: Bb\n', '        D: Dd\n']
        )

    def test_move_back_twice(self):
        paragraph = ['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n']
        line = Line('    B: Bb\n', paragraph)
        line.move_back()
        line.move_back()
        self.assertEqual(paragraph, 
            ['A:\n', '    E:\n', '    B: Bb\n', '        C: Cc\n', '        D: Dd\n']
        )

    def test_move_back_first_element(self):
        paragraph = ['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n']
        line = Line('A:\n', paragraph)
        with self.assertRaises(IndexError):
            line.move_back()
                
if __name__ == '__main__':
    unittest.main()