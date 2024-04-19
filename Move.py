from Constants import *
import numpy as np
from Bitboard_helpers import *
from Board import *

'''
          binary move bits                               hexidecimal constants
    
    0000 0000 0000 0000 0011 1111    source square       0x3f
    0000 0000 0000 1111 1100 0000    target square       0xfc0
    0000 0000 1111 0000 0000 0000    piece               0xf000
    0000 1111 0000 0000 0000 0000    promoted piece      0xf0000
'''


class Move:
    

    @classmethod
    def encode_move(cls,src,dest,piece,promo):
        move=np.uint32(0)
        move|=np.uint32(src)
        move|=np.uint32(dest<<6)
        move|=np.uint32(piece<<12)
        move|=np.uint32(promo<<16)

        return move
  
    @classmethod
    def get_move_src(cls,move):
        return move & 0x3f
    
    @classmethod
    def get_move_dest(cls,move):
        return (move & 0xfc0)>>6
    
    @classmethod
    def get_move_piece(cls,move):
        return (move & 0xf000)>>12
    
    @classmethod
    def get_move_promo(cls,move):
        return (move & 0xf0000)>>16
    

    @classmethod
    def print_move(cls,move):
        print("bestmove %s%s%s" % (square_map[Move.get_move_src(move)],square_map[Move.get_move_dest(move)],Piece.promoted_pieces[Move.get_move_promo(move)]),flush=True)
        

                                
'''                            
board=Board()
board.initialize_board()
board=board.make_move(Move,Move.encode_move(square_indices['e2'],square_indices['e4'],0,0))
board.print_board()


'''