#!/usr/bin/env python3
from sys import argv, exit
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

def interpretArgument(argument, argv, default_value):
    if (
            argument in argv
            and argv.index(argument) < len(argv) - 1
            and argv.count(argument) ==1
        ):
        return int(argv[argv.index(argument) + 1])
    else:
        return default_value


def readArguments(argv):
    size = interpretArgument("-s", argv, 3)
    size = interpretArgument("--size", argv, size)
    level = interpretArgument("-l", argv, 3)
    level = interpretArgument("--level", argv, level)
    if "--repeat" in argv or "-r" in argv:
        repeat = "Y"
    else:
        repeat = "N"
    if size < 3:
        size = 3

    return [size, level, repeat]

def makeBoard(size, space="_"):
    return [[space for row in range(size)] for column in range(size)]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.button = board
        self.resize(300, 250)

        box = QGroupBox(self)
        box.setGeometry(70,10,140,140)

        difficultyDial = QSlider(self)
        difficultyDial.setGeometry(10,10,50,30)
        difficultyDial.setOrientation(Qt.Horizontal)

        difficulty = QLCDNumber(self)
        difficulty.setGeometry(10,32,50,20)

        for row in range(len(board)):
            for column in range(len(board)):
                self.button[row][column] = QPushButton(" ", self)
                self.button[row][column].setGeometry(40*column+80,40*row+20,40,40)
                self.button[row][column].clicked.connect(lambda: self.button[row][column].setText("X"))

if __name__ == "__main__":
    arglist = readArguments(argv)
    board = makeBoard(arglist[0], "_")
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
