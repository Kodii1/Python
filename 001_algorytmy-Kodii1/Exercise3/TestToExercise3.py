import unittest

from Exercise3 import repairRange

class TestExercise3(unittest.TestCase):
    def test_first(self):
        n = 5
        result = repairRange(n)
        expected = 3
        self.assertEqual(result, expected)
    def test_secound(self):
        n = 1
        result = repairRange(n)
        expected = 1
        self.assertEqual(result, expected)
    def test_third(self):
        n = 2
        result = repairRange(n)
        expected = 1
        self.assertEqual(result, expected)
    def test_forth(self):
        n = 6
        result = repairRange(n)
        expected = 5
        self.assertEqual(result, expected)
    def test_fifth(self):
        n = -200
        result = repairRange(n)
        expected = "It's not passive number"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()