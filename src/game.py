import pygame

from const import *
from board import Board
from square import Square


class Game:
    def __init__(self):
        self.ai = True
        self.nextPlayer = 'X'
        self.hovered_sqr = None
        self.board = Board()
        pygame.font.init()

    def show_bg(self, surface):

        for row in range(ROWS):
            for col in range(COLS):
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, BOARD, rect)

        for col in range(COLS + 1):
            x = col * SQSIZE
            pygame.draw.line(surface, GRID, (x, 0), (x, ROWS * SQSIZE), 3)

        for row in range(ROWS + 1):
            y = row * SQSIZE
            pygame.draw.line(surface, GRID, (0, y), (COLS * SQSIZE, y), 3)

    def show_mark(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if not self.board.squares[row][col].isempty():
                    mark = self.board.squares[row][col].mark
                    rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                    if mark == "X":

                        line_thickness = 7
                        cross_length = int(0.90 * SQSIZE / 2)
                        center = (rect[0] + SQSIZE // 2, rect[1] + SQSIZE // 2)

                        pygame.draw.line(surface, COLOR_X, (center[0] - cross_length, center[1] - cross_length),
                                         (center[0] + cross_length, center[1] + cross_length), line_thickness)
                        pygame.draw.line(surface, COLOR_X, (center[0] - cross_length, center[1] + cross_length),
                                         (center[0] + cross_length, center[1] - cross_length), line_thickness)

                    else:

                        center = (rect[0] + SQSIZE // 2, rect[1] + SQSIZE // 2)
                        radius = SQSIZE // 2 - 3
                        pygame.draw.circle(surface, COLOR_O, center, radius, 7)

    def show_hover(self, surface):
        if self.hovered_sqr:
            color = (180, 180, 180)
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            pygame.draw.rect(surface, color, rect, width=3)

    def set_hover(self, row, col):
        if col > 2:
            col = 2
        if row > 2:
            row = 2
        self.hovered_sqr = self.board.squares[row][col]

    def next_turn(self):
        self.nextPlayer = 'X' if self.nextPlayer == 'O' else 'O'
        if self.ai:
            if self.nextPlayer == 'O':
                return True

        return False

    def reset(self):
        self.__init__()
