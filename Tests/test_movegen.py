import sys
sys.path.append('..')
from movegen import *


def test_generate_moves():
    b=Board()
    b.initialize_board()
    b.print_board()
    movelist=generate_moves(b)
    for move in movelist:
        print(move)

    print(len(movelist))

def test_generate_moves_black():
    b=Board()
    b.initialize_board()
    b.print_board()
    b.color_to_move=(b.color_to_move^1)
    movelist=generate_moves(b)
    for move in movelist:
        print(move)

    print(len(movelist))

def test_generate_moves_after_move():
    b=Board()
    b.initialize_board()
    b.print_board()
    b.update_from_fen("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 1")
    b.print_board()
    movelist=generate_moves(b)
    for move in movelist:
        print(move)

    print(len(movelist))



test_generate_moves_after_move()
