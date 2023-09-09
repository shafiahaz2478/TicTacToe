import copy

from const import *
from square import Square


def check(board, mark):
    if board.check_win(mark):
        return mark

    if board.check_draw():
        return 'Tie'

    return False


def play_move(board):
    mark = 'X'

    alpha = float("-inf")
    beta = float("inf")
    bestscore, best_square = minimax(board, 8, alpha, beta, mark)

    move = (best_square.row, best_square.col)

    print(f'AI has chosen to mark the square in pos {move} with an eval of: {bestscore}')

    return best_square


def minimax(board, depth, alpha, beta, mark):
    result = check(board, mark)
    mark = 'X' if mark == 'O' else 'O'
    if result:
        if result == 'X':
            return depth, None
        elif result == 'O':
            return -depth, None
        else:
            return 0, None
    if mark == 'X':
        bestscore = float("-inf")
        best_square = None
        for row in range(ROWS):
            for col in range(COLS):
                if board.squares[row][col].isempty():
                    temp_board = copy.deepcopy(board)
                    temp_board.squares[row][col] = Square(row, col, mark)
                    score = minimax(temp_board, depth - 1, alpha, beta, mark)[0]

                    if score > bestscore:
                        bestscore = score
                        best_square = temp_board.squares[row][col]
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return bestscore , best_square

    else:
        bestscore = float("inf")
        for row in range(ROWS):
            for col in range(COLS):
                if board.squares[row][col].isempty():
                    temp_board = copy.deepcopy(board)
                    temp_board.squares[row][col] = Square(row, col, mark)
                    score = minimax(temp_board, depth - 1, alpha, beta, mark)[0]

                    if score < bestscore:
                        bestscore = score
                        best_square = temp_board.squares[row][col]
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return bestscore, best_square
