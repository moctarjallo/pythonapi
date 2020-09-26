import unittest

import pythonapi as api

class TestTupleDictRequest(unittest.TestCase):
    def test_simple(self):
        data = ({'a':1}, {'b':2}, {'c':3})
        req = api.TupleDictRequest(data)
        self.assertEqual(req.data, {
            'a': 1,
            'b': 2,
            'c': 3
        })

    def test_imbricated_tuple_in_dict_value(self):
        data = ({'a':({'d': 4}, {'e': 5})}, {'b':2}, {'c':3})
        req = api.TupleDictRequest(data)
        self.assertEqual(req.data, {
            'a': {
                'd':4,
                'e':5
            },
            'b': 2,
            'c': 3
        })

    def test_triply_imbricated_tuple_in_dict_value(self):
        data = ({'a':1}, {'b':({'f':({'d':4}, {'e':5})},)}, {'c':3})
        req = api.TupleDictRequest(data)
        self.assertEqual(req.data, {
            'a': 1,
            'b': {
                'f':{
                    'd':4,
                    'e':5
                }
            },
            'c': 3
        })

if __name__ == '__main__':
    unittest.main()