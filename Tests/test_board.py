import sys
sys.path.append('..')
from Board import *
from Move import *  

def update_from_fen():
    #Test 1 :Check whether the Board is getting updated from the FEN string
    new_board=Board()
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    new_board.update_from_fen(fen)
    new_board.print_board()

def make_move():
    #Test 2 :Check whether the move is getting made correctly
    new_board=Board()
    new_board.initialize_board()
    new_board.print_board()
    new_board=new_board.make_move(Move,Move.encode_move(52,36,0,0))
    new_board.print_board()

def initialize_board():
    #Test 3 :Check whether the Board is getting initialized correctly
    new_board=Board()
    new_board.initialize_board()
    new_board.print_board()

initialize_board()



