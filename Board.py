import numpy as np
from Bitboard_helpers import *

square_indices = {
    'a8': 0, 'b8': 1, 'c8': 2, 'd8': 3, 'e8': 4, 'f8': 5, 'g8': 6, 'h8': 7,
    'a7': 8, 'b7': 9, 'c7': 10, 'd7': 11, 'e7': 12, 'f7': 13, 'g7': 14, 'h7': 15,
    'a6': 16, 'b6': 17, 'c6': 18, 'd6': 19, 'e6': 20, 'f6': 21, 'g6': 22, 'h6': 23,
    'a5': 24, 'b5': 25, 'c5': 26, 'd5': 27, 'e5': 28, 'f5': 29, 'g5': 30, 'h5': 31,
    'a4': 32, 'b4': 33, 'c4': 34, 'd4': 35, 'e4': 36, 'f4': 37, 'g4': 38, 'h4': 39,
    'a3': 40, 'b3': 41, 'c3': 42, 'd3': 43, 'e3': 44, 'f3': 45, 'g3': 46, 'h3': 47,
    'a2': 48, 'b2': 49, 'c2': 50, 'd2': 51, 'e2': 52, 'f2': 53, 'g2': 54, 'h2': 55,
    'a1': 56, 'b1': 57, 'c1': 58, 'd1': 59, 'e1': 60, 'f1': 61, 'g1': 62, 'h1': 63,
}

class Board:
    def __init__(self):

        self.white_R=np.uint64(0)
        self.white_N = np.uint64(0)
        self.white_B = np.uint64(0)
        self.white_Q = np.uint64(0)
        self.white_K = np.uint64(0)
        self.white_P = np.uint64(0)

        self.black_R = np.uint64(0)
        self.black_N = np.uint64(0)
        self.black_B = np.uint64(0)
        self.black_Q = np.uint64(0)
        self.black_K = np.uint64(0)
        self.black_P = np.uint64(0)
    
    
    
    def initialize_board(self):
        for square in ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']:
            self.white_P = set_bit(self.white_P, square_indices[square])
        self.white_R = set_bit(self.white_R, square_indices['a1'])
        self.white_R = set_bit(self.white_R, square_indices['h1'])
        self.white_N = set_bit(self.white_N, square_indices['b1'])
        self.white_N = set_bit(self.white_N, square_indices['g1'])
        self.white_B = set_bit(self.white_B, square_indices['c1'])
        self.white_B = set_bit(self.white_B, square_indices['f1'])
        self.white_Q = set_bit(self.white_Q, square_indices['d1'])
        self.white_K = set_bit(self.white_K, square_indices['e1'])

 
        for square in ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']:
            self.black_P = set_bit(self.black_P, square_indices[square])
        self.black_R = set_bit(self.black_R, square_indices['a8'])
        self.black_R = set_bit(self.black_R, square_indices['h8'])
        self.black_N = set_bit(self.black_N, square_indices['b8'])
        self.black_N = set_bit(self.black_N, square_indices['g8'])
        self.black_B = set_bit(self.black_B, square_indices['c8'])
        self.black_B = set_bit(self.black_B, square_indices['f8'])
        self.black_Q = set_bit(self.black_Q, square_indices['d8'])
        self.black_K = set_bit(self.black_K, square_indices['e8'])

    
   



b = Board()
b.initialize_board()

all_bitboards = b.white_R | b.white_N | b.white_B | b.white_Q | b.white_K | b.white_P | b.black_R | b.black_N | b.black_B | b.black_Q | b.black_K | b.black_P
print_bitboard(all_bitboards)
print("White Rooks:")
print_bitboard(b.white_R)
print("White Knights:")
print_bitboard(b.white_N)
print("White Bishops:")
print_bitboard(b.white_B)
print("White Queen:")
print_bitboard(b.white_Q)
print("White King:")
print_bitboard(b.white_K)
print("White Pawns:")
print_bitboard(b.white_P)

print("Black Rooks:")
print_bitboard(b.black_R)
print("Black Knights:")
print_bitboard(b.black_N)
print("Black Bishops:")
print_bitboard(b.black_B)
print("Black Queen:")
print_bitboard(b.black_Q)
print("Black King:")
print_bitboard(b.black_K)
print("Black Pawns:")
print_bitboard(b.black_P)



