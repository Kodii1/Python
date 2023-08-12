import unittest

from Exercise4 import sortDates

class TestExercise4(unittest.TestCase):
    def test_first(self):
        dates = {}
        for i in range(10):
            dates.update({i:{"day":1,"month":2,"year":5}})
        result = sortDates(dates)
        expected = {0: {'day': 1, 'month': 2, 'year': 5}, 1: {'day': 1, 'month': 2, 'year': 5}, 2: {'day': 1, 'month': 2, 'year': 5}, 3: {'day': 1, 'month': 2, 'year': 5}, 4: {'day': 1, 'month': 2, 'year': 5}, 5: {'day': 1, 'month': 2, 'year': 5}, 6: {'day': 1, 'month': 2, 'year': 5}, 7: {'day': 1, 'month': 2, 'year': 5}, 8: {'day': 1, 'month': 2, 'year': 5}, 9: {'day': 1, 'month': 2, 'year': 5}}
        self.assertEqual(result, expected)
        
    def test_secound(self):
        dates = {}
        for i in range(10):
            dates.update({i:{"day":1,"month":2,"year":i}})
        result = sortDates(dates)
        expected = {0: {'day': 1, 'month': 2, 'year': 0}, 1: {'day': 1, 'month': 2, 'year': 1}, 2: {'day': 1, 'month': 2, 'year': 2}, 3: {'day': 1, 'month': 2, 'year': 3}, 4: {'day': 1, 'month': 2, 'year': 4}, 5: {'day': 1, 'month': 2, 'year': 5}, 6: {'day': 1, 'month': 2, 'year': 6}, 7: {'day': 1, 'month': 2, 'year': 7}, 8: {'day': 1, 'month': 2, 'year': 8}, 9: {'day': 1, 'month': 2, 'year': 9}}
        self.assertEqual(result, expected)

    def test_third(self):
        dates = {}
        for i in range(0,10):
            dates.update({i:{"day":10-i,"month":10-i,"year":10-i}})
        result = sortDates(dates)
        expected ={0: {'day': 9, 'month': 9, 'year': 9}, 1: {'day': 8, 'month': 8, 'year': 8}, 2: {'day': 7, 'month': 7, 'year': 7}, 3: {'day': 6, 'month': 6, 'year': 6}, 4: {'day': 5, 'month': 5, 'year': 5}, 5: {'day': 4, 'month': 4, 'year': 4}, 6: {'day': 3, 'month': 3, 'year': 3}, 7: {'day': 2, 'month': 2, 'year': 2}, 8: {'day': 1, 'month': 1, 'year': 1}, 9: {'day': 10, 'month': 10, 'year': 10}}
        self.assertEqual(result, expected)


    def test_fourth(self):
        dates = {}
        dates.update({0:{"day":13,"month":15,"year":2019}})
        dates.update({1:{"day":18,"month":16,"year":200}})
        dates.update({2:{"day":16,"month":20,"year":15665}})
        result = sortDates(dates)
        expected = {0: {'day': 18, 'month': 16, 'year': 200}, 1: {'day': 13, 'month': 15, 'year': 2019}, 2: {'day': 16, 'month': 20, 'year': 15665}}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()