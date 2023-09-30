#!/usr/bin/env python3
from sys import argv, exit
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGroupBox

size = 3
board = [['_' for row in range(size)] for column in range(size)]
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300, 250)

        self.button = board

        box = QGroupBox(self)
        box.setGeometry(70,10,140,140)

        for row in range(len(board)):
            for column in range(len(board)):
                self.button[row][column] = QPushButton(' ', self)
                self.button[row][column].setGeometry(40*column+80,40*row+20,40,40)
                self.button[row][column].clicked.connect(lambda r=row, c=column: self.on_square_clicked(r, c))
    def on_square_clicked(self, row, column):
        if self.button[row][column].text == "X":
            text = "O"
        else:
            text = "X"
        self.button[row][column].setText(text)

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
