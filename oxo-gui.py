#!/usr/bin/env python3
from sys import argv, exit
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGroupBox, QSlider, QLCDNumber

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
                self.button[row][column].clicked.connect(self.on_button_click)
    def on_button_click(self):
        print(self.button[row][column])

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
