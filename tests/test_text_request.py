import unittest

import pythonapi as api

class TestTextRequest(unittest.TestCase):
    def test_0level_1line_paragraph(self):
        paragraph = [['FIRSTNAME: Moctar\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'firstname': 'moctar'
        }])

    def test_0level_1line_paragraph_with_tab(self):
        paragraph = [['  FIRSTNAME: Moctar\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'firstname': 'moctar'
        }])

        paragraph = [['LASTNAME: Diallo\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'lastname': 'diallo'
        }])

    def test_0level_2line_paragraph(self):
        paragraph = [['FIRSTNAME: Moctar\n', 'LASTNAME: Diallo\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'firstname': 'moctar',
            'lastname': 'diallo'
        }])

    def test_0level_3line_paragraph(self):
        paragraph = [['FIRSTNAME: Moctar\n', 'LASTNAME: Diallo\n', 'ADDRESS: medina\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'firstname': 'moctar',
            'lastname': 'diallo',
            'address': 'medina'
        }])

    def test_1level_1line_paragraph(self):
        paragraph = [['CLIENT:\n', '    FIRSTNAME: Moctar\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'client':{
                'firstname': 'moctar'
            }
        }])

        
    # @unittest.skip("Test later")
    def test_1level_2line_paragraph(self):
        paragraph = [['CLIENT:\n', '    FIRSTNAME: Moctar\n', '    LASTNAME: Diallo\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'client': {
                'firstname': 'moctar',
                'lastname': 'diallo',
            }
        }])

    def test_1level_3line_paragraph(self):
        paragraph = [['CLIENT:\n', '    FIRSTNAME: Moctar\n', '    LASTNAME: Diallo\n', '    ADDRESS: Medina\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'client': {
                'firstname': 'moctar',
                'lastname': 'diallo',
                'address': 'medina'
            }
        }])

    def test_1level_Nline_paragraph(self):
        paragraph = [['A:\n', '    B: Bb\n', '    C: Cc\n', '    D: Dd\n', '    E: Ee\n', '    F: Ff\n', '    G: Gg\n', '    H: Hh\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'a': {
                'b': 'bb',
                'c': 'cc',
                'd': 'dd',
                'e': 'ee',
                'f': 'ff',
                'g': 'gg',
                'h': 'hh'
            }
        }])

    def test_2level_1line_paragraph(self):
        paragraph = [['A:\n', 'B:\n', '      C: Cc\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'a':{
                'b': {
                    'c': 'cc'
                }
            }
        }])

    def test_2level_2line_paragraph(self):
        paragraph = [['A:\n', 'B:\n', '    C: Cc\n', '    D: Dd\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'a':{
                'b': {
                    'c': 'cc',
                    'd': 'dd'
                }
            }
        }])

    def test_double2level_2line_paragraph(self):
        paragraph = [['A:\n', '    E: Ee\n', '    B:\n', '        C: Cc\n', '        D: Dd\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'a':{
                'e': 'ee',
                'b': {
                    'c': 'cc',
                    'd': 'dd'
                }
            }
        }])

    def test_double2level_2line_paragraph_ending_with_line(self):
        paragraph = [['A:\n', '    E:\n', '        C: Cc\n', '        D: Dd\n', '    B: Bb\n']]
        request = api.TextRequest(paragraph)
        self.assertEqual(request.data, [{
            'a':{
                'e': {
                    'c': 'cc',
                    'd': 'dd'
                },
                'b': 'bb'
            }
        }])

if __name__ == '__main__':
    unittest.main()