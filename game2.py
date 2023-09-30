import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)

        self.current_player = 'X'
        self.grid = [['' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None, None, None], [None, None, None], [None, None, None]]

        for i in range(3):
            for j in range(3):
                button = QPushButton(self)
                button.setGeometry(i * 100, j * 100, 100, 100)
                button.clicked.connect(lambda _, row=i, col=j: self.button_click(row, col))
                self.buttons[i][j] = button

    def button_click(self, row, col):
        if self.grid[row][col] == '':
            self.grid[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            if self.check_winner(row, col):
                self.show_winner_message()
                self.reset_game()
            elif self.check_draw():
                self.show_draw_message()
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        player = self.grid[row][col]
        # Check row
        if all(self.grid[row][i] == player for i in range(3)):
            return True
        # Check column
        if all(self.grid[i][col] == player for i in range(3)):
            return True
        # Check diagonals
        if (row == col and all(self.grid[i][i] == player for i in range(3))) or \
           (row + col == 2 and all(self.grid[i][2 - i] == player for i in range(3))):
            return True
        return False

    def check_draw(self):
        return all(self.grid[i][j] != '' for i in range(3) for j in range(3))

    def show_winner_message(self):
        winner = self.current_player
        msg = QMessageBox()
        msg.setWindowTitle("Game Over")
        msg.setText(f"Player {winner} wins!")
        msg.exec_()

    def show_draw_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Game Over")
        msg.setText("It's a draw!")
        msg.exec_()

    def reset_game(self):
        self.current_player = 'X'
        self.grid = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText('')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
