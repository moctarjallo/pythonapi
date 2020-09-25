import unittest

from pythonapi import TextResponse

class TestTextResponse(unittest.TestCase):
    def test_simple_dict(self):
        response = TextResponse([{
            'firstname': "moctar",
            'age': 27
        }])
        self.assertEqual(response.data, 
"""
FIRSTNAME: Moctar
AGE: 27
"""
        )

    def test_many_items_in_dict(self):
        response = TextResponse([{
            'firstname': 'moctar',
            'lastname': 'diallo',
            'address': 'medina',
            'balance': 5000
        }])
        self.assertEqual(response.data,
"""
FIRSTNAME: Moctar
LASTNAME: Diallo
ADDRESS: Medina
BALANCE: 5000
"""
        )

    def test_imbricated_dict(self):
        response = TextResponse([{
            'client': {
                'firstname': 'moctar',
                'lastname': 'diallo'
            },
            'balance': 5000
        }])

        self.assertEqual(response.data,
"""
CLIENT:
    FIRSTNAME: Moctar
    LASTNAME: Diallo
BALANCE: 5000
"""
        )

    def test_adjacently_imbricated_dicts(self):
        response = TextResponse([{
            'account': {
                'client': {
                    'firstname': 'moctar',
                    'lastname': 'diallo'
                },
            'balance': 5000
            }
        }])
        # print(response.data)

        self.assertEqual(response.data,
"""
ACCOUNT:
    CLIENT:
        FIRSTNAME: Moctar
        LASTNAME: Diallo
    BALANCE: 5000
"""
        )

if __name__ == '__main__':
    unittest.main()
