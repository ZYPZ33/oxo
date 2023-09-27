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

size = 3
board = [["_" for row in range(size)] for column in range(size)]
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.button = board

        self.resize(300, 250)

        box = QGroupBox(self)
        box.setGeometry(70,10,140,140)

        difficultyDial = QSlider(self)
        difficultyDial.setGeometry(220,160,50,30)
        difficultyDial.setOrientation(Qt.Horizontal)

        difficulty = QLCDNumber(self)
        difficulty.setGeometry(220,190,50,20)

        for row in range(len(board)):
            for column in range(len(board)):
                self.button[row][column] = QPushButton("X", self)
                self.button[row][column].setGeometry(40*column+80,40*row+20,40,40)
                self.button[row][column].clicked.connect(lambda: self.on_button_click(row,column))
    def on_button_click(self,x,y):
        print(self.button[x][y].text())

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
