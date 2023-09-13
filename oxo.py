#!/usr/bin/env python3
from random import choice
from os import name, system

enemydot = "X"
playerdot = "O"
acceptable_values = [0, 1, 2]
dot2name = {playerdot: "player", enemydot: "enemy"}


def clear():
    if name == "posix":
        _ = system("clear")
    if name == "nt":
        _ = system("cls")


def makeboard():
    return [["_" for row in range(3)] for column in range(3)]


def placesLeft(board):
    spaces = 0
    for row in board:
        for area in row:
            if area == "_":
                spaces += 1
    return spaces


def printboard(b):
    return f"____1___2___3____\n1|  {b[0][0]}\
 | {b[1][0]} | {b[2][0]}  |\n2|  {b[0][1]}\
 | {b[1][1]} | {b[2][1]}  |\n3|  {b[0][2]}\
 | {b[1][2]} | {b[2][2]}  |"


def placedot(board, placer):
    originalBoard = board
    if not findWinner(board):
        while originalBoard == board:
            if placesLeft(board) == 0:
                return board
            if placer == "player":
                x = int(input("Enter x coordinate: ")) - 1
                y = int(input("Enter y coordinate: ")) - 1
                dot = playerdot
            else:
                nextPlaces = findAboutToWin(board, playerdot, enemydot)
                if nextPlaces:
                    x = nextPlaces[0]
                    y = nextPlaces[1]
                else:
                    x = choice(acceptable_values)
                    y = choice(acceptable_values)
                dot = enemydot
            if x in acceptable_values:
                if y in acceptable_values:
                    if board[x][y] == "_":
                        board[x][y] = dot
                        return board
                    else:
                        if placer == "player":
                            print("Space already filled")
                else:
                    if placer == "player":
                        print(f"{y+1} not a valid Y coordinate")
            else:
                if placer == "player":
                    print(f"{x+1} not a valid X coordinate")
    else:
        return board


def findWinner(board):
    row = list()
    for placerdot in [playerdot, enemydot]:
        winningThree = [placerdot, placerdot, placerdot]
        for column in board:
            if column == winningThree:
                return dot2name[placerdot]
        if board[1][1] == placerdot:
            if board[0][0] == placerdot and board[2][2] == placerdot:
                return dot2name[placerdot]
            if board[2][0] == placerdot and board[0][2] == placerdot:
                return dot2name[placerdot]
        for i in range(3):
            for j in range(3):
                row.append(board[j][i])
            if row == winningThree:
                return dot2name[placerdot]
            row = []


def findAboutToWin(board, threatdot, gooddot):
    for x in range(len(board)):
        column = board[x]
        if column.count(threatdot) == 2 and column.count(gooddot) < 1:
            y = column.index("_")
            return [x, y]
    if board[1][1] == threatdot:
        if board[0][0] == threatdot and board[2][2] != gooddot:
            return [2, 2]
        if board[0][2] == threatdot and board[2][0] != gooddot:
            return [2, 0]
        if board[2][2] == threatdot and board[0][0] != gooddot:
            return [0, 0]
        if board[2][0] == threatdot and board[0][2] != gooddot:
            return [0, 2]
    for x in range(3):
        row = list()
        for y in range(3):
            row.append(board[y][x])
        if row.count(threatdot) == 2 and row.count(gooddot) < 1:
            y = row.index("_")
            return [y, x]


# init
board = makeboard()
if __name__ == "__main__":
    playgame = True
    while playgame:
        clear()
        if placesLeft(board) > 0 and not findWinner(board):
            print(printboard(board))
            board = placedot(board, "player")
            board = placedot(board, "enemy")
        else:
            print(printboard(board))
            print("Game over")
            winner = findWinner(board)
            if winner:
                print(f"{winner} wins")
            else:
                print("draw")
            playgame = False
