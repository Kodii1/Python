import unittest

from pierwszy import (changeHetmans, changePawn, createHetman, createPlaces,
                      killingPawn)


class TestExercise4(unittest.TestCase):
    def test_createPlaces(self):
        size = 8
        board = [[' ' for x in range(size)] for y in range(size)]
        expected = 1
        result = 0
        createPlaces(size, board, "H")
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'H':
                    result += 1
        self.assertEqual(result, expected)

    def test_changePawn(self):
        size = 8
        board = [[' ' for x in range(size)] for y in range(size)]
        positionPawn = [1, 2]
        board[positionPawn[0]][positionPawn[1]] = 'P'
        expected = 1
        result = 0
        changePawn(size, board, positionPawn)
        if board[positionPawn[0]][positionPawn[1]] == ' ':
            for i in range(size):
                for j in range(size):
                    if board[i][j] == 'P':
                        result += 1
        self.assertEqual(result, expected)

    def test_createHetman(self):
        size = 8
        expected = 3
        result = 0
        board = [[' ' for x in range(size)] for y in range(size)]
        createHetman(size, board, expected)
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'H':
                    result += 1
        self.assertEqual(result, expected)

    def test_changeHetmans(self):
        result = 0
        expected = 2
        size = 8
        board = [[' ' for x in range(size)] for y in range(size)]
        positionsHetman = [[1, 1]]
        board[positionsHetman[0][0]][positionsHetman[0][1]] = 'H'
        if board[positionsHetman[0][0]][positionsHetman[0][1]] == 'H':
            result += 1
        positionToDelte = [1, 1]
        changeHetmans(positionsHetman, positionToDelte, board, size)

        if board[positionToDelte[0]][positionToDelte[1]] == ' ':
            result += 1
        self.assertEqual(result, expected)

    def test_killingPawn(self):
        size = 8
        board = [[' ' for x in range(size)] for y in range(size)]
        positionPawn = [0, 0]
        board[positionPawn[0]][positionPawn[1]] = "P"
        positionsHetman = [[1, 1], [0, 3], [3, 0], [2, 5]]
        expected = 3
        for i in range(len(positionsHetman)):
            board[positionsHetman[i][0]][positionsHetman[i][1]] = 'H'
        result = killingPawn(positionPawn, positionsHetman)
        self.assertEqual(len(result), expected)


if __name__ == '__main__':
    unittest.main()
