import copy
import glubo

from const import *
from square import Square


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0] for _ in range(COLS)]
        self._create()

    def apply(self, col, row, mark):
        self.squares[row][col] = Square(row, col, mark)
        if self.check_win(mark):
            print(mark + " has won")
            return True

        if self.check_draw():
            print("Its a draw")
            return True

        return False

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def check_win(self, mark):
        for row in range(3):
            if all(square.mark == mark for square in self.squares[row]):
                return True

        for col in range(3):
            if all(self.squares[row][col].mark == mark for row in range(3)):
                return True

        # Check main diagonal (top-left to bottom-right)
        if all(self.squares[i][i].mark == mark for i in range(3)):
            return True

        # Check secondary diagonal (top-right to bottom-left)
        if all(self.squares[i][2 - i].mark == mark for i in range(3)):
            return True

        return False

    def check_draw(self):
        draw = True
        for row in range(ROWS):
            for col in range(COLS):
                if self.squares[row][col].isempty():
                    draw = False

        return draw

    def ai(self):
        return glubo.play_move(self)
