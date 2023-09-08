import sys

import pygame

from const import *
from game import Game


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("TicTacToe")
        self.game = Game()

    def mainloop(self):
        screen = self.screen
        game = self.game
        board = game.board
        ended = False

        while True:
            game.show_bg(screen)
            game.show_mark(screen)
            game.show_hover(screen)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_row = event.pos[1] // SQSIZE
                    clicked_col = event.pos[0] // SQSIZE

                    if board.squares[clicked_row][clicked_col].isempty():
                        if not ended:
                            ended = board.apply(clicked_col, clicked_row, game.nextPlayer)
                            if not ended:
                                if game.next_turn():
                                    ai_move = board.ai()
                                    ended = board.apply(ai_move.col, ai_move.row, game.nextPlayer)
                                    game.next_turn()

                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset()
                        screen = self.screen
                        game = self.game
                        board = game.board
                        ended = False
                    elif event.key == pygame.K_g:
                        game.ai = not game.ai

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
