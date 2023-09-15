#!/usr/bin/env python3
from random import choice
from os import name, system
from sys import argv

if "-h" in argv or "--help" in argv:
    print(
        "Usage: oxo OPTION... [FILE]...\n\
    --help  -h\tPrint this help message\n\
    --size  -s\tSet the size of the game board (must be greater than 3)\n\
    --level -l\tSet the AI level (1-3)"
    )
    exit()


def clear():
    if name == "posix":
        system("clear")
    if name == "nt":
        system("cls")


def interpretArgument(argument, argv, default_value):
    if (
        argument in argv
        and argv.index(argument) < len(argv) - 1
        and argv.count(argument) == 1
    ):
        return int(argv[argv.index(argument) + 1])
    else:
        return default_value


def readArguments(argv):
    size = interpretArgument("-s", argv, 3)
    level = interpretArgument("-l", argv, 3)
    size = interpretArgument("--size", argv, size)
    level = interpretArgument("--level", argv, size)
    if size < 3:
        size = 3
    return [size, level]


def makeBoard(size, space="_"):
    return [[space for row in range(size)] for column in range(size)]


def printBoard(board):
    for row in board:
        for item in row:
            print(item, end=" ")
        print()


def takeTurn(board, placer, size, dotdictionary, level):
    acceptableValues = list(range(size))
    originalBoard = board
    while (
        board == originalBoard
        and not boardEmpty(board)
        and not findWinner(board, dotdictionary)
    ):
        if placer == "player":
            dot = dotdictionary[placer]
            correct = False
            col = 2
            row = 2
            while not correct:
                col = input("Enter X coordinate: ")
                row = input("Enter Y coordinate: ")
                if col.isnumeric() and row.isnumeric():
                    col = int(col) - 1
                    row = int(row) - 1
                    correct = True
        else:
            nextcoords = list()
            dot = "X"
            if (
                realCount(board, "_") == (size**2 - 1)
                and board[1][1] == "_"
                and level > 2
            ):
                nextcoords = [1, 1]
            else:
                if level > 2:
                    nextcoords = findNextCoords(board, "X")
            if not nextcoords and level > 1:
                nextcoords = findNextCoords(board, "O")
            if nextcoords:
                row = nextcoords[0]
                col = nextcoords[1]
            else:
                row = choice(acceptableValues)
                col = choice(acceptableValues)
        if row in acceptableValues:
            if col in acceptableValues:
                if board[row][col] == "_":
                    board[row][col] = dot
                    return board
                else:
                    if placer == "player":
                        print("Not an available space")
            else:
                print(f"Not acceptable value: {int(col)+1}")
        else:
            print(f"Not acceptable value: {int(row)+1}")


def realCount(array, character):
    count = 0
    for row in array:
        count += row.count(character)
    return count


def findWinner(board, dotdictionary):
    for placer in dotdictionary:
        dot = dotdictionary[placer]
        for row in board:
            if row.count(dot) == 3:
                return placer
        for i in range(len(board)):
            column = list()
            for j in range(len(board)):
                column.append(board[j][i])
            if column.count(dot) == 3:
                return placer
        if board[1][1] == dot:
            if board[0][0] == dot and board[2][2] == dot:
                return placer
            if board[0][2] == dot and board[2][0] == dot:
                return placer
    return False


def findNextCoords(board, threatDot):
    for row in range(len(board)):
        if board[row].count(threatDot) == 2 and "_" in board[row]:
            return [row, board[row].index("_")]
    for i in range(len(board)):
        column = list()
        for j in range(len(board)):
            column.append(board[j][i])
        if column.count(threatDot) == 2 and "_" in column:
            return [column.index("_"), i]
    if board[1][1] == threatDot:
        if board[0][0] == threatDot and board[2][2] == "_":
            return [2, 2]
        if board[2][2] == threatDot and board[0][0] == "_":
            return [0, 0]
        if board[0][2] == threatDot and board[2][0] == "_":
            return [2, 0]
        if board[2][0] == threatDot and board[0][2] == "_":
            return [0, 2]


def boardEmpty(board):
    for row in board:
        if "_" in row:
            return False
    return True


def game(arglist):
    board = makeBoard(arglist[0])
    dotdictionary = {"player": "O", "computer": "X"}
    while not boardEmpty(board) and not findWinner(board, dotdictionary):
        clear()
        printBoard(board)
        takeTurn(board, "player", arglist[0], dotdictionary, arglist[1])
        takeTurn(board, "computer", arglist[0], dotdictionary, arglist[1])
    if findWinner(board, dotdictionary):
        clear()
        printBoard(board)
        print(f"Winner is the {findWinner(board, dotdictionary)}!")
        return 0
    else:
        print("Game is a draw")
        return 0


if __name__ == "__main__":
    arglist = readArguments(argv)
    game(arglist)
