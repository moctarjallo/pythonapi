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

    def test_basic_with_dict_in_inputs(self):
        data = ('a', '1'), {'b': 2}
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

    def test_simple_imbrication_with_dict_inputs(self):
        data = ({'a': (('d', '4'), ('e', 5))},)
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

    def test_triply_imbricated_tuple_with_dict_inputs(self):
        data = (('a',1), 
                ('b',(
                    {'f':(
                        {'d':'4'}, 
                        {'e': 5}
                        )
                    },
                    )
                ), 
                ('c',3)
                )
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'a': 1,
            'b': {
                'f':{
                    'd':4.0,
                    'e':5
                }
            },
            'c': 3.0
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

    def test_transaction_request_using_tuples(self):
        data = (('action', 'deposit'), 
                ('amount', 2000), 
                ('account', (
                    ('code', '2520'), 
                    ('balance', '5000'), 
                    ('client', (
                        ('address', 'plateau'), 
                        ('lastname', 'ba'), 
                        ('firstname', 'amadou')
                        ))
                    )
                )
            )
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'action': 'deposit',
            'amount': 2000.0,
            'account': {
                'code': 2520.0,
                'balance': 5000.0,
                'client': {
                    'address': 'plateau',
                    'lastname': 'ba',
                    'firstname': 'amadou'
                }
            }
        })

def test_transaction_request_using_dicts_in_inputs(self):
        ill_data = (('action', 'deposit'), ('amount', 2000), ('account', {'code': '2520', 'balance': '5000', 'client': {'address': 'thiaroye', 'lastname': 'ba', 'firstname': 'amadou'}}))
        req = api.TupleRequest(ill_data)
        self.assertEqual(req.data, {
            'action': 'deposit',
            'amount': 2000.0,
            'account': {
                'code': 2520.0,
                'balance': 5000.0,
                'client': {
                    'address': 'plateau',
                    'lastname': 'ba',
                    'firstname': 'amadou'
                }
            }
        })

if __name__ == '__main__':
    unittest.main()