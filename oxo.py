#!/usr/bin/env python3
from random import randint
from os import system
from time import sleep

acceptable_values = [1, 2, 3]
playerdot = "O"
enemydot = "X"


def clear():
    system("clear")


def makeboard(size):
    return [["_" for row in range(3)] for column in range(3)]


def placesLeft(board):
    spaces = 0
    for row in board:
        for area in row:
            if area == "_":
                spaces += 1
    return spaces


def printboard(b):
    return f"____1___2___3____\n1|  {b[0][0]} | {b[1][0]} | {b[2][0]}  |\n2|  {b[0][1]} | {b[1][1]} | {b[2][1]}  |\n3|  {b[0][2]} | {b[1][2]} | {b[2][2]}  |"


def placedot(board, placer):
    while True:
        if placesLeft(board) != 0:
            if placer == "player":
                xcoord = int(input("Enter x coordinate: "))
                ycoord = int(input("Enter y coordinate: "))
                dot = playerdot
            else:
                xcoord = randint(1, 3)
                ycoord = randint(1, 3)
                dot = enemydot
            if xcoord in acceptable_values and ycoord in acceptable_values:
                if board[xcoord - 1][ycoord - 1] == "_":
                    area_available = True
                    if (
                        xcoord in acceptable_values
                        and ycoord in acceptable_values
                        and area_available
                    ):
                        board[xcoord - 1][ycoord - 1] = dot
                        return board
                    elif (
                        xcoord not in acceptable_values
                        or ycoord not in acceptable_values
                    ):
                        print(
                            f"Please re-enter values: either {xcoord}\
                            not allowed or {ycoord} not allowed"
                        )
                else:
                    return False


# init
board = makeboard(5)
if __name__ == "__main__":
    print(printboard(board))
    playgame = True
    while playgame:
        if placesLeft(board) > 0:
            print(placesLeft(board), "left")
            newboard = placedot(board, "player")
            if newboard is not False:
                board = newboard
            newboard = placedot(board, "cpu")
            if newboard is not False:
                board = newboard
            clear()
            print(printboard(board))
        else:
            print("Game over")
            sleep(2)
            exit()
