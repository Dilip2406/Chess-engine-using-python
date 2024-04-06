from Bitboard_helpers import *
from Board import *
from Move import *


def generate_moves(board:Board):
        movelist=[]
        if board.color_to_move==Color.WHITE:
            for piece ,bitboard in board.white_pieces_dict.items():
            
                while bitboard :
                    
                    if piece==Piece.wP:
                        
                        source_square=get_lsb(bitboard)
                        attacks=get_pawn_attacks(source_square,'white') & board.black_pieces_bb
                       
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wP,0))
                            attacks=pop_bit(attacks,dest_square)
                        pushes=get_pawn_pushes(source_square,'white') & ~board.occupancy_squares_bb
                        while(pushes):
                            dest_square=get_lsb(pushes)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wP,0))
                            pushes=pop_bit(pushes,dest_square)
                        bitboard=pop_lsb(bitboard)
                    if piece==Piece.wK:
                        
                        source_square=get_lsb(bitboard)
                        attacks=get_king_attacks(source_square) & board.black_pieces_bb
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wK,0))
                            attacks=pop_bit(attacks,dest_square)
                        moves=get_king_attacks(source_square) & ~board.occupancy_squares_bb
                        while(moves):
                            dest_square=get_lsb(moves)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wK,0))
                            moves=pop_bit(moves,dest_square)
                        bitboard=pop_lsb(bitboard)
                    if piece==Piece.wN:
                        
                        source_square=get_lsb(bitboard)
                        attacks=get_knight_attacks(source_square) & board.black_pieces_bb
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wN,0))
                            attacks=pop_bit(attacks,dest_square)
                        moves=get_knight_attacks(source_square) & ~board.occupancy_squares_bb
                        while(moves):
                            dest_square=get_lsb(moves)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wN,0))
                            moves=pop_bit(moves,dest_square)
                        bitboard=pop_lsb(bitboard)
                    if piece==Piece.wB:
                        
                        source_square=get_lsb(bitboard)
                        attacks=get_bishop_attacks(source_square,board.occupancy_squares_bb) & board.black_pieces_bb
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wB,0))
                            attacks=pop_bit(attacks,dest_square)
                        moves=get_bishop_attacks(source_square,board.occupancy_squares_bb) & ~board.occupancy_squares_bb
                        while(moves):
                            dest_square=get_lsb(moves)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wB,0))
                            moves=pop_bit(moves,dest_square)
                        bitboard=pop_lsb(bitboard)
                    if piece==Piece.wR:
                        
                        source_square=get_lsb(bitboard)
                        attacks=get_rook_attacks(source_square,board.occupancy_squares_bb) & board.black_pieces_bb
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wR,0))
                            attacks=pop_bit(attacks,dest_square)
                        moves=get_rook_attacks(source_square,board.occupancy_squares_bb) & ~board.occupancy_squares_bb
                        while(moves):
                            dest_square=get_lsb(moves)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wR,0))
                            moves=pop_bit(moves,dest_square)
                        bitboard=pop_lsb(bitboard)
                    if piece==Piece.wQ:
                        
                        source_square=get_lsb(bitboard)
                        attacks=get_queen_attacks(source_square,board.occupancy_squares_bb) & board.black_pieces_bb
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wQ,0))
                            attacks=pop_bit(attacks,dest_square)
                        moves=get_queen_attacks(source_square,board.occupancy_squares_bb) & ~board.occupancy_squares_bb
                        while(moves):
                            dest_square=get_lsb(moves)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.wQ,0))
                            moves=pop_bit(moves,dest_square)
                        bitboard=pop_lsb(bitboard)
        
        if board.color_to_move==Color.BLACK:
            for piece ,bitboard in board.black_pieces_dict.items():
                while bitboard:
                    if piece==Piece.bP:
                        
                        source_square=get_lsb(bitboard)
                        attacks=get_pawn_attacks(source_square,'black') & board.white_pieces_bb
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bP,0))
                            attacks=pop_bit(attacks,dest_square)
                        pushes=get_pawn_pushes(source_square,'black') & ~board.occupancy_squares_bb
                        while(pushes):
                            dest_square=get_lsb(pushes)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bP,0))
                            pushes=pop_bit(pushes,dest_square)
                        bitboard=pop_lsb(bitboard)
                    if piece==Piece.bK:
                        source_square=get_lsb(bitboard)
                        attacks=get_king_attacks(source_square) & board.white_pieces_bb
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bK,0))
                            attacks=pop_bit(attacks,dest_square)
                        moves=get_king_attacks(source_square) & ~board.occupancy_squares_bb
                        while(moves):
                            dest_square=get_lsb(moves)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bK,0))
                            moves=pop_bit(moves,dest_square)
                        bitboard=pop_lsb(bitboard)
                    if piece==Piece.bN:
                        source_square=get_lsb(bitboard)
                        attacks=get_knight_attacks(source_square) & board.white_pieces_bb
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bN,0))
                            attacks=pop_bit(attacks,dest_square)
                        moves=get_knight_attacks(source_square) & ~board.occupancy_squares_bb
                        while(moves):
                            dest_square=get_lsb(moves)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bN,0))
                            moves=pop_bit(moves,dest_square)
                        bitboard=pop_lsb(bitboard)
                    if piece==Piece.bB:
                        source_square=get_lsb(bitboard)
                        attacks=get_bishop_attacks(source_square,board.occupancy_squares_bb) & board.white_pieces_bb
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bB,0))
                            attacks=pop_bit(attacks,dest_square)
                        moves=get_bishop_attacks(source_square,board.occupancy_squares_bb) & ~board.occupancy_squares_bb
                        while(moves):
                            dest_square=get_lsb(moves)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bB,0))
                            moves=pop_bit(moves,dest_square)
                        bitboard=pop_lsb(bitboard)
                    if piece==Piece.bR:
                        source_square=get_lsb(bitboard)
                        attacks=get_rook_attacks(source_square,board.occupancy_squares_bb) & board.white_pieces_bb
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bR,0))
                            attacks=pop_bit(attacks,dest_square)
                        moves=get_rook_attacks(source_square,board.occupancy_squares_bb) & ~board.occupancy_squares_bb
                        while(moves):
                            dest_square=get_lsb(moves)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bR,0))
                            moves=pop_bit(moves,dest_square)
                        bitboard=pop_lsb(bitboard)
                    if piece==Piece.bQ:
                        source_square=get_lsb(bitboard)
                        attacks=get_queen_attacks(source_square,board.occupancy_squares_bb) & board.white_pieces_bb
                        while(attacks):
                            dest_square=get_lsb(attacks)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bQ,0))
                            attacks=pop_bit(attacks,dest_square)
                        moves=get_queen_attacks(source_square,board.occupancy_squares_bb) & ~board.occupancy_squares_bb
                        while(moves):
                            dest_square=get_lsb(moves)
                            movelist.append(Move.encode_move(source_square,dest_square,Piece.bQ,0))
                            moves=pop_bit(moves,dest_square)
                        bitboard=pop_lsb(bitboard)    
        return movelist

