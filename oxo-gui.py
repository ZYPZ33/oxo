#!/usr/bin/env python3
from sys import argv, exit
from random import choice
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGroupBox, QSlider, QLCDNumber

if "-h" in argv or "--help" in argv:
    print(
        "Usage: oxo OPTION...\n\
    --help   -h\tPrint this help message\n\
    --size   -s\tSet the size of the game board (must be greater than 3)\n\
    --level  -l\tSet the AI level (1-3)\n\
    --repeat -r\tMake game loop"
          )
    exit()

def interpretArgument(argument, argv, defaultValue):
    if (
            argument in argv
            and argv.index(argument) < len(argv) - 1
            and argv.count(argument) ==1
        ):
        return int(argv[argv.index(argument) + 1])
    else:
        return defaultValue


def readArguments(argv):
    size = interpretArgument('-s', argv, 3)
    size = interpretArgument("--size", argv, size)
    level = interpretArgument('-l', argv, 3)
    level = interpretArgument("--level", argv, level)
    if "--repeat" in argv or '-r' in argv:
        repeat = 'Y'
    else:
        repeat = 'N'
    if size < 3:
        size = 3

    return [size, level, repeat]

def makeBoard(size, space=' '):
    return [[space for row in range(size)] for column in range(size)]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.playerDot='O'
        self.enemyDot='X'
        self.placer = "player"
        self.spacer = ''

        arglist = readArguments(argv)
        self.board = makeBoard(arglist[0], self.spacer)
        self.button = makeBoard(arglist[0], None)
        self.sizeValue = arglist[0]
        self.level = arglist[1]
        self.repeatOn = arglist[2]

        self.resize(300, 250)

        box = QGroupBox(self)
        box.setGeometry(70,10,140,140)

        difficultyDial = QSlider(self)
        difficultyDial.setGeometry(10,10,50,30)
        difficultyDial.setOrientation(Qt.Horizontal)

        difficulty = QLCDNumber(self)
        difficulty.setGeometry(10,32,50,20)

        for row in range(len(self.board)):
            for column in range(len(self.board)):
                self.button[row][column] = QPushButton(' ', self)
                self.button[row][column].setGeometry(40*column+80,40*row+20,40,40)
                self.button[row][column].clicked.connect(lambda _, r=row, c=column: self.on_square_clicked(r, c))

    def on_square_clicked(self, row, column):
        for i in range(2):
            if self.placer == "player":
                if self.board[row][column] == self.spacer:
                    self.placer = "inactive"
                    self.board[row][column] = self.playerDot
                    self.button[row][column].setText(self.playerDot)
                    self.placer="enemy"
            elif self.placer == "enemy":
                length = len(self.board)-1
                center = length//2
                self.player = "inactive"
                nextcoords=list()
                if self.twoDcount(self.board, self.spacer) == (self.sizeValue**2 -1) and self.level > 2:
                    if self.board[center][center] == self.spacer:
                        nextcoords=[center, center]
                    else:
                        nextcoords=[choice([0,length]),choice([0,length])]
                elif self.level > 2:
                    nextcoords=self.findNextCoords(self.board, self.enemyDot)
                elif self.level > 1:
                    nextcoords=self.findNextCoords(self.board, self.playerDot)
                if self.level < 1 or nextcoords == [None, None]:
                    if self.twoDcount(self.board, self.spacer) > 0:
                        nextcoords=[choice(list(range(length))),choice(list(range(length)))]
                        while self.board[nextcoords[0]][nextcoords[1]] != self.spacer:
                            nextcoords=[choice(list(range(length))),choice(list(range(length)))]
                    else:
                        exit()

                self.board[nextcoords[0]][nextcoords[1]] = (self.enemyDot)
                self.button[nextcoords[0]][nextcoords[1]].setText(self.enemyDot)
                self.placer="player"


    def twoDcount(self, array, character):
        count = 0
        for row in array:
            count += row.count(character)
        return count

    def findNextCoords(self, board, threatDot):
        length = len(board)
        center = length // 2
        for row in range(length):
            if board[row].count(threatDot) == length-1 and self.spacer in board[row]:
                return [row, board[row].index(self.spacer)]
        for i in range(length):
            column = list()
            for j in range(length):
                column.append(board[j][i])
            if column.count(threatDot) == length-1 and self.spacer in column:
                return [column.index(self.spacer), i]
        if board[center][center] == threatDot:
            if board[0][0] == threatDot and board[2][2] == self.spacer:
                return [2, 2]
            if board[2][2] == threatDot and board[0][0] == self.spacer:
                return [0, 0]
            if board[0][2] == threatDot and board[2][0] == self.spacer:
                return [2, 0]
            else:
                return [0, 2]
        return [None, None]

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
