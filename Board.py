import numpy as np
from Bitboard_helpers import *

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
    def black_pieces_dict(self):
        return {Piece.bP:self.black_P,Piece.bR:self.black_R,Piece.bN:self.black_N,Piece.bB:self.black_B,Piece.bQ:self.black_Q,Piece.bK:self.black_K}
    
    @property
    def white_pieces_dict(self):
        return {Piece.wP:self.white_P,Piece.wR:self.white_R,Piece.wN:self.white_N,Piece.wB:self.white_B,Piece.wQ:self.white_Q,Piece.wK:self.white_K}
    
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
        if fen_parts[1]=='w':
            self.color_to_move=Color.WHITE
        else:
            self.color_to_move=Color.BLACK

                

    

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

    def is_in_check(self, square, side):
        if side == 'white':
            if get_pawn_attacks(square, 'black') & self.Piece_bb[Piece.wP]:
                return True
        else:
            if get_pawn_attacks(square, 'white') & self.Piece_bb[Piece.bP]:
                return True
        if get_knight_attacks(square) & self.Piece_bb[Piece.wN if side == 'white' else Piece.bN]:
            return True
        if get_king_attacks(square) & self.Piece_bb[Piece.wK if side == 'white' else Piece.bK]:
            return True
        if get_bishop_attacks(square,self.occupancy_squares_bb) & (self.Piece_bb[Piece.wB if side=='white' else Piece.bB] | self.Piece_bb[Piece.wQ if side=='white' else Piece.bQ]):
            return True
        if get_rook_attacks(square,self.occupancy_squares_bb) & (self.Piece_bb[Piece.wR if side=='white' else Piece.bR] | self.Piece_bb[Piece.wQ if side=='white' else Piece.bQ]):
            return True
        return False
    
    def get_piece_on_square(self, square):
        if self.white_B & (np.uint64(1) <<np.uint64(square)):
            return "white_B"
        elif self.white_K & (np.uint64(1) <<np.uint64(square)):
            return "white_K"
        elif self.white_N & (np.uint64(1) <<np.uint64(square)):
            return "white_N"
        elif self.white_P & (np.uint64(1) <<np.uint64(square)):
            return "white_P"
        elif self.white_Q & (np.uint64(1) <<np.uint64(square)):
            return "white_Q"
        elif self.white_R & (np.uint64(1) <<np.uint64(square)):
            return "white_R"
        elif self.black_B & (np.uint64(1) <<np.uint64(square)):
            return "black_B"
        elif self.black_K & (np.uint64(1) <<np.uint64(square)):
            return "black_K"
        elif self.black_N & (np.uint64(1) <<np.uint64(square)):
            return "black_N"
        elif self.black_P & (np.uint64(1) <<np.uint64(square)):
            return "black_P"
        elif self.black_Q & (np.uint64(1) <<np.uint64(square)):
            return "black_Q"
        elif self.black_R & (np.uint64(1) <<np.uint64(square)):
            return "black_R"
        
        return None

    def make_move(self, m,move):
        new_board = Board()
        new_board.white_R = self.white_R
        new_board.white_N = self.white_N
        new_board.white_B = self.white_B
        new_board.white_Q = self.white_Q
        new_board.white_K = self.white_K
        new_board.white_P = self.white_P

        new_board.black_R = self.black_R
        new_board.black_N = self.black_N
        new_board.black_B = self.black_B
        new_board.black_Q = self.black_Q
        new_board.black_K = self.black_K
        new_board.black_P = self.black_P

        new_board.color_to_move = self.color_to_move
        source=m.get_move_src(move)
        target=m.get_move_dest(move)

        piece=new_board.get_piece_on_square(source)
        target_piece=new_board.get_piece_on_square(target)
        setattr(new_board,piece,pop_bit(getattr(new_board,piece),source))
        if target_piece:
            setattr(new_board,target_piece,pop_bit(getattr(new_board,target_piece),target))
        setattr(new_board,piece,set_bit(getattr(new_board,piece),target))
        if self.color_to_move==Color.WHITE:
            if self.is_in_check(get_lsb(self.white_K),self.color_to_move):
                return None
            
        elif self.color_to_move==Color.BLACK:
            if self.is_in_check(get_lsb(self.white_K),self.color_to_move):
                return None
            
        new_board.color_to_move=(new_board.color_to_move ^ 1)
       ## new_board.print_board()
    
        return new_board
        







