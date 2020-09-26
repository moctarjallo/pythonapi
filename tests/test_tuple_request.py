import unittest

import pythonapi as api

class TestTupleRequest(unittest.TestCase):
    def test_simple(self):
        keys = ['a', 'b', 'c']
        values = (1, 2, 3)
        req = api.TupleRequest(keys, values)
        self.assertEqual(req.data, {
            'a': 1,
            'b': 2,
            'c': 3
        })

if __name__ == '__main__':
    unittest.main()