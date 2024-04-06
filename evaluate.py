from Bitboard_helpers import *
from Board import *



def evaluate(board:Board):
    
    white_pawns = board.white_P
    white_knights = board.white_N
    white_bishops = board.white_B
    white_rooks = board.white_R
    white_queens = board.white_Q
   
    black_pawns = board.black_P
    black_knights = board.black_N
    black_bishops = board.black_B
    black_rooks = board.black_R
    black_queens = board.black_Q
   
    white_score = 0
    black_score = 0
    white_score += count_bits(white_pawns) * 100
    white_score += count_bits(white_knights) * 320
    white_score += count_bits(white_bishops) * 330
    white_score += count_bits(white_rooks) * 500
    white_score += count_bits(white_queens) * 900
    black_score += count_bits(black_pawns) * 100
    black_score += count_bits(black_knights) * 320
    black_score += count_bits(black_bishops) * 330
    black_score += count_bits(black_rooks) * 500
    black_score += count_bits(black_queens) * 900


    return (white_score - black_score)/100



