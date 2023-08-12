import unittest
from Exercise2 import friendlyNumbers

class TestZadanie2(unittest.TestCase):
    def test_first(self):
        minRange = 100
        maxRange = 200
        result = friendlyNumbers(minRange,maxRange)
        expected = []
        self.assertEqual(result, expected)
    def test_secound(self):
        minRange = 12000
        maxRange = 13000
        result = friendlyNumbers(minRange,maxRange)
        expected = [[12285, 14595]]
        self.assertEqual(result, expected)
    def test_third(self):
        minRange = 5000
        maxRange = 6000
        result = friendlyNumbers(minRange,maxRange)
        expected = [[5020, 5564]]
        self.assertEqual(result, expected)
    def test_forth(self):
        minRange = 100
        maxRange = 2000
        result = friendlyNumbers(minRange,maxRange)
        expected = [[220, 284],[1184, 1210]]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()