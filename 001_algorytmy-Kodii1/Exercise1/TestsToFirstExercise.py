import unittest
from Exercise1 import primeNumbers

class TestZadanie1(unittest.TestCase):
    def test_first(self):
        minNumber = 2
        maxNumber = 10
        result = primeNumbers(minNumber,maxNumber)
        expected = [ 2, 3, 5, 7]
        self.assertEqual(result, expected)

    def test_second(self):
        minNumber = -1
        maxNumber = 11
        result = primeNumbers(minNumber,maxNumber)
        expected = [ 2, 3, 5, 7, 11]
        self.assertEqual(result, expected)

    def test_third(self):
        minNumber = 0
        maxNumber = 13
        result = primeNumbers(minNumber,maxNumber)
        expected = [ 2, 3, 5, 7,11 ,13]
        self.assertEqual(result, expected)

    def test_fourth(self):
        minNumber = 6
        maxNumber = 20
        result = primeNumbers(minNumber,maxNumber)
        expected = [7, 11 ,13 ,17 ,19]
        self.assertEqual(result, expected)
    
if __name__ == '__main__':
    unittest.main()