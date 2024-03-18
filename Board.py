import numpy as np
from Bitboard_helpers import *
from Piece import *
from Color import *
from fen import generate_fen
from Constants import *

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

        self.color_to_move = None
        self.castle_rights=[[None,None],[None,None]]
        self.en_passant_target=None
    
    @property
    def Piece_bb(self):
        Piece_bb={Piece.wP:self.white_P,Piece.wR:self.white_R,Piece.wN:self.white_N,Piece.wB:self.white_B,Piece.wQ:self.white_Q,Piece.wK:self.white_K,Piece.bP:self.black_P,Piece.bR:self.black_R,Piece.bN:self.black_N,Piece.bB:self.black_B,Piece.bQ:self.black_Q,Piece.bK:self.black_K}
        return Piece_bb  
    
    @property
    def white_pieces_bb(self):
        return self.white_R | self.white_N | self.white_B | self.white_Q | self.white_K | self.white_P
    
    @property
    def black_pieces_bb(self):
        return self.black_R | self.black_N | self.black_B | self.black_Q | self.black_K | self.black_P
    
    @property
    def occupancy_squares_bb(self):
        return self.white_pieces_bb | self.black_pieces_bb
    
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

        self.castle_rights[Color.WHITE][0]=True
        self.castle_rights[Color.WHITE][1]=True
        self.castle_rights[Color.BLACK][0]=True
        self.castle_rights[Color.BLACK][1]=True

        self.color_to_move=Color.WHITE
        
        self.en_passant_target=None 

    def update_from_fen(self, position):
        fen_parts = position.split(' ')
        board_layout = fen_parts[0]
        board_layout = board_layout.split('/')
        rank = 0
        file = 0
        Board.clear_bitboards(self)

        for char in board_layout:
            for symbol in char:
                if symbol.isalpha():
                    square = rank * 8 + file
                    bitboard = np.uint64(1 << square)
                    piece = Piece.piece_map[symbol]
                    setattr(self, piece, set_bit(getattr(self, piece),square))
                    file += 1
                elif symbol.isdigit():
                    file += int(symbol)
            rank += 1
            file = 0

                

    

    def clear_bitboards(self):
        self.white_R = np.uint64(0)
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

    def print_board(self):
        board = np.zeros((8, 8), dtype=str)
        for square in range(64):
            if get_bit(self.white_R, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.wR]
            elif get_bit(self.white_N, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.wN]
            elif get_bit(self.white_B, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.wB]
            elif get_bit(self.white_Q, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.wQ]
            elif get_bit(self.white_K, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.wK]
            elif get_bit(self.white_P, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.wP]
            elif get_bit(self.black_R, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.bR]
            elif get_bit(self.black_N, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.bN]
            elif get_bit(self.black_B, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.bB]
            elif get_bit(self.black_Q, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.bQ]
            elif get_bit(self.black_K, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.bK]
            elif get_bit(self.black_P, square):
                board[square // 8, square % 8] = piece_to_glyph[Piece.bP]
            
            else: 
                board[square // 8, square % 8] = '.'
            

        for row in range(8):
            print(8 - row, end='  ')
            print(' '.join(board[row]))

        print('   a b c d e f g h')
        print()
    

b = Board()
b.initialize_board()

fen = "r1bk3r/p2pBpNp/n4n2/1p1NP2P/6P1/3P4/P1P1K3/q5b1 w KQkq - 0 0"

b.update_from_fen(fen)


print_bitboard(b.white_pieces_bb | b.black_pieces_bb)

b.print_board() 

print(fen)
print(fen==generate_fen(b))



