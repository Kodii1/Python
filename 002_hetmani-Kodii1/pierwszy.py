import secrets


def createPlaces(size, board, whatIsIt):     # create board with pawn or hetmans
    xy = [secrets.randbelow(size), secrets.randbelow(size)]

    if board[xy[0]][xy[1]] == 'H' or board[xy[0]][xy[1]] == 'P':
        return createPlaces(size, board, whatIsIt)
    else:
        board[xy[0]][xy[1]] = whatIsIt
        return xy


# create Pawn 1st pawn and also chage position of pawn
def changePawn(size, board, position=False):
    if position:
        board[position[0]][position[1]] = ' '
    return createPlaces(size, board, "P")


def createHetman(size, board, n):  # create Hetmans and storage theit positions in 2 D array
    positions = []
    for i in range(n):
        positions.append(createPlaces(size, board, "H"))
    return positions


# change hetman position or delete hetman
def changeHetmans(positionsHetman, positionToDelte, board, size, delete=False):

    for i in range(len(positionsHetman)):
        if positionsHetman[i][0:len(positionsHetman[0])] == positionToDelte[0:len(positionToDelte)]:
            positionsHetman.pop(i)
            break
    else:
        print("Podano złe wartości taki Hetman nie Istnieje")
        return positionsHetman
    board[positionToDelte[0]][positionToDelte[1]] = ' '  # delete old hetman
    if not delete:
        positionsHetman.append(createPlaces(size, board, "H"))
        board[positionsHetman[len(positionsHetman)-1][0]
              ][positionsHetman[len(positionsHetman)-1][1]] = 'H'
    return positionsHetman


def printBoard(board, size):  # printing a board with X elements in row
    for i in range(size-1, -1, -1):
        print(board[i][0:size])
    print("\n")


def killingPawn(positionPawn, positionsHetman):  # looking can hetman kill pawn
    arrayGodHetman = set()
    for i in range(len(positionsHetman)):
        if positionPawn[1] == positionsHetman[i][1]:
            arrayGodHetman.add(tuple(positionsHetman[i]))

        if positionPawn[0] == positionsHetman[i][0]:
            arrayGodHetman.add(tuple(positionsHetman[i]))

        if abs(positionPawn[1]-positionsHetman[i][1]) == abs(positionPawn[0]-positionsHetman[i][0]):
            arrayGodHetman.add(tuple(positionsHetman[i]))
    if len(arrayGodHetman) == 0:
        print("Żaden hetman nie bije pionka \n")
        return False
    else:
        print(
            f'Pionek jest bity przez hetmanów na pozycjach (y,x): {arrayGodHetman} \n')
        return arrayGodHetman


# printing hetmans who can kill pawn
def printKillingHetmans(arrayGodHetman, positionPawn, size):
    array = list(arrayGodHetman)
    killingBoard = [[' ' for x in range(size)] for y in range(size)]
    killingBoard[positionPawn[0]][positionPawn[1]] = 'P'

    for i in range(len(array)):
        killingBoard[array[i][0]][array[i][1]] = 'H'

    printBoard(killingBoard, size)


if __name__ == "__main__":
    hetman = int(input('Wpisz ilość hetmanów: '))
    size = int(input('Wpisz wielkość planszy: '))

    board = [[' ' for x in range(size)] for y in range(size)]  # creating board
    positionToDelte = []

    # array with position pawn
    positionPawn = changePawn(size, board)
    # array with position Hetman
    positionsHetman = createHetman(size, board, hetman)

    printBoard(board, size)

    # array with hetmans who can kill pawn
    arrayGodHetman = killingPawn(positionPawn, positionsHetman)

    if arrayGodHetman:
        printKillingHetmans(arrayGodHetman, positionPawn, size)

        change = int(input('Jeżeli chcesz zmienić miejsce piąka wpisz "1": '))

        if change == 1:
            # array with position pawn
            positionPawn = changePawn(size, board, positionPawn)
            change = 0
            # array with position Hetman
            arrayGodHetman = killingPawn(positionPawn, positionsHetman)
            printKillingHetmans(arrayGodHetman, positionPawn, size)

        if len(arrayGodHetman) > 0:
            change = int(
                input('Jeżeli chcesz zmienić miejsce hetmana wpisz "1": '))

            if change == 1:
                positionToDelte = [int(input("PODAJ OS Y (wartośći od dołu liczone): ")), int(
                    input("PODAJ OS X (wartośći od góry lewej): "))]
                change = 0
                positionsHetman = changeHetmans(
                    positionsHetman, positionToDelte, board, size)  # array with position pawn
                # array with position hetman
                arrayGodHetman = killingPawn(positionPawn, positionsHetman)
                if arrayGodHetman:  # if any of hetmans can kill pawn - False
                    printKillingHetmans(arrayGodHetman, positionPawn, size)

                    change = int(
                        input('Jeżeli chcesz ununąć miejsce hetmana wpisz "1": '))

                    if change == 1:
                        positionToDelte = [int(input("PODAJ OS Y (wartośći od dołu liczone): ")), int(
                            input("PODAJ OS X (wartośći od góry lewej): "))]
                        change = 0
                        positionsHetman = changeHetmans(
                            positionsHetman, positionToDelte, board, size, True)  # array with position pawn
                        # array with position Hetman
                        arrayGodHetman = killingPawn(
                            positionPawn, positionsHetman)
                        if arrayGodHetman:  # if any of hetmans can kill pawn - False
                            printKillingHetmans(
                                arrayGodHetman, positionPawn, size)
