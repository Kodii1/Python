import unittest

from Exercise4 import sortDates

class TestExercise4(unittest.TestCase):
    def test_first(self):
        dates = []
        for i in range(10):
            dates.append({'d': 1, 'm': 2, 'r': 5})
        result = sortDates(dates)
        expected = [{'d': 1, 'm': 2, 'r': 5}, {'d': 1, 'm': 2, 'r': 5}, {'d': 1, 'm': 2, 'r': 5}, 
                    {'d': 1, 'm': 2, 'r': 5}, {'d': 1, 'm': 2, 'r': 5}, {'d': 1, 'm': 2, 'r': 5}, 
                    {'d': 1, 'm': 2, 'r': 5}, {'d': 1, 'm': 2, 'r': 5}, {'d': 1, 'm': 2, 'r': 5}, 
                    {'d': 1, 'm': 2, 'r': 5}]
        self.assertEqual(result, expected)
        
    def test_secound(self):
        dates = []
        for i in range(10):
            dates.append({"d":1,"m":2,"r":i})
        result = sortDates(dates)
        expected = [{'d': 1, 'm': 2, 'r': 0},{'d': 1, 'm': 2, 'r': 1},{'d': 1, 'm': 2, 'r': 2}, 
                    {'d': 1, 'm': 2, 'r': 3}, {'d': 1, 'm': 2, 'r': 4},{'d': 1, 'm': 2, 'r': 5},
                    {'d': 1, 'm': 2, 'r': 6},{'d': 1, 'm': 2, 'r': 7}, {'d': 1, 'm': 2, 'r': 8},{'d': 1, 'm': 2, 'r': 9}]
        self.assertEqual(result, expected)

    def test_third(self):
        dates = []
        for i in range(9,0,-1):
            dates.append({"d":i,"m":i,"r":i})
        result = sortDates(dates)
        expected = [{'d': 1, 'm': 1, 'r': 1}, {'d': 2, 'm': 2, 'r': 2}, {'d': 3, 'm': 3, 'r': 3}, 
                    {'d': 4, 'm': 4, 'r': 4}, {'d': 5, 'm': 5, 'r': 5}, {'d': 6, 'm': 6, 'r': 6},
                     {'d': 7, 'm': 7, 'r': 7}, {'d': 8, 'm': 8, 'r': 8}, {'d': 9, 'm': 9, 'r': 9}]
        self.assertEqual(result, expected)

    def test_fourth(self):
        dates = []
        dates.append({"d":13,"m":15,"r":2019})
        dates.append({"d":18,"m":16,"r":200})
        dates.append({"d":16,"m":20,"r":15665})
        result = sortDates(dates)
        expected = [{'d': 18, 'm': 16, 'r': 200},{'d': 13, 'm': 15, 'r': 2019},{'d': 16, 'm': 20, 'r': 15665}]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()