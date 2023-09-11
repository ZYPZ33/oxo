#!/usr/bin/env python3
from random import choice
from os import system, name

acceptable_values = [0, 1, 2]
playerdot = "O"
enemydot = "X"


def clear():
    if name == "postix":
        system("clear")


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


# def placedot(board, placer):
# while True:
# if placesLeft(board) != 0:
# if placer == "player":
# xcoord = int(input("Enter x coordinate: "))
# ycoord = int(input("Enter y coordinate: "))
# dot = playerdot
# else:
# xcoord = randint(1, 3)
# ycoord = randint(1, 3)
# dot = enemydot
# if xcoord in acceptable_values and ycoord in acceptable_values:
# if board[xcoord - 1][ycoord - 1] == "_":
# board[xcoord - 1][ycoord - 1] = dot
# return board
# else:
# print("Not available")
# else:
# print(f"not an accepted value: either {xcoord} or {ycoord}")


def placedot2(board, placer):
    originalBoard = board
    while originalBoard == board:
        if placesLeft(board) == 0:
            return board
        if placer == "player":
            x = int(input("Enter x coordinate: ")) - 1
            y = int(input("Enter y coordinate: ")) - 1
            dot = playerdot
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
                    print("Space already filled")
            else:
                print(f"{y+1} not a valid Y coordinate")
        else:
            print(f"{x+1} not a valid X coordinate")


def findWinner(board):
    column = list()
    dot2name = {playerdot: "player", enemydot: "enemy"}
    for placerdot in [playerdot, enemydot]:
        for row in board:
            if row == [placerdot, placerdot, placerdot]:
                return dot2name[placerdot]
        if board[1][1] == placerdot:
            if board[0][0] == placerdot and board[2][2] == placerdot:
                return dot2name[placerdot]
            if board[2][0] == placerdot and board[0][2] == placerdot:
                return dot2name[placerdot]
        for i in range(3):
            for j in range(3):
                column.append(board[i][j])
            print(column)


# init
board = makeboard()
if __name__ == "__main__":
    playgame = True
    while playgame:
        if placesLeft(board) > 0:
            print(printboard(board))
            board = placedot2(board, "player")
            board = placedot2(board, "enemy")
            # clear()
        else:
            print("Game over")
            print(f"{findWinner(board)} wins")
            playgame = False
