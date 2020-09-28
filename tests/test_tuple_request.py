import unittest

import pythonapi as api

class TestTupleRequest(unittest.TestCase):
    def test_basic(self):
        data = ('a', 1),
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'a': 1,
        })

    def test_basic_with_string_value(self):
        data = ('a', '1'), ('b', 2)
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'a': 1,
            'b': 2
        })

    def test_simple(self):
        data = (('a', 1), ('b', 2), ('c', 3))
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'a': 1,
            'b': 2,
            'c': 3
        })

    def test_simple_imbrication(self):
        data = (('a', (('d', 4), ('e', 5))),)
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'a': {
                'd':4,
                'e':5
            }
        })

    def test_simple_imbrication_with_string_value(self):
        data = (('a', (('d', '4'), ('e', 5))),)
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'a': {
                'd':4,
                'e':5
            }
        })

    def test_simple_imbrication_with_string_value_of_float(self):
        data = (('a', (('d', '4.2'), ('e', 5))),)
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'a': {
                'd':4.2,
                'e':5
            }
        })

    def test_imbricated_tuple_in_dict_value(self):
        data = (('a', (('d', 4), ('e', 5))), ('b',2), ('c', 3,))
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'a': {
                'd':4,
                'e':5
            },
            'b': 2,
            'c': 3
        })

    def test_triply_imbricated_tuple_in_dict_value(self):
        data = (('a',1), 
                ('b',(
                    ('f',(
                        ('d',4), 
                        ('e',5)
                        )
                    ),
                    )
                ), 
                ('c',3)
                )
        req = api.TupleRequest(data)
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

    def test_triply_imbricated_tuple_in_dict_value_and_string_numbers(self):
        data = (('a',1), 
                ('b',(
                    ('f',(
                        ('d','4.1'), 
                        ('e',5)
                        )
                    ),
                    )
                ), 
                ('c',3)
                )
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'a': 1,
            'b': {
                'f':{
                    'd':4.1,
                    'e':5
                }
            },
            'c': 3
        })


if __name__ == '__main__':
    unittest.main()