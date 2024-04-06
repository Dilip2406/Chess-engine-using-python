import numpy as np


from Constants import *


def generate_fen(board) -> str:
    """
    Generates an FEN given the provided board
    """
    black_pawn_bin = np.binary_repr(board.black_P, 64)
    black_rook_bin = np.binary_repr(board.black_R, 64)
    black_knight_bin = np.binary_repr(board.black_N, 64)
    black_bishop_bin = np.binary_repr(board.black_B, 64)
    black_queen_bin = np.binary_repr(board.black_Q, 64)
    black_king_bin = np.binary_repr(board.black_K, 64)
    white_pawn_bin = np.binary_repr(board.white_P, 64)
    white_rook_bin = np.binary_repr(board.white_R, 64)
    white_knight_bin = np.binary_repr(board.white_N, 64)
    white_bishop_bin = np.binary_repr(board.white_B, 64)
    white_queen_bin = np.binary_repr(board.white_Q, 64)
    white_king_bin = np.binary_repr(board.white_K, 64)

    black_pawn_squares = [i for i in range(len(black_pawn_bin)) if int(black_pawn_bin[i])]
    black_rook_squares = [i for i in range(len(black_rook_bin)) if int(black_rook_bin[i])]
    black_knight_squares = [i for i in range(len(black_knight_bin)) if int(black_knight_bin[i])]
    black_bishop_squares = [i for i in range(len(black_bishop_bin)) if int(black_bishop_bin[i])]
    black_queen_squares = [i for i in range(len(black_queen_bin)) if int(black_queen_bin[i])]
    black_king_square = [i for i in range(len(black_king_bin)) if int(black_king_bin[i])]
    white_pawn_squares = [i for i in range(len(white_pawn_bin)) if int(white_pawn_bin[i])]
    white_rook_squares = [i for i in range(len(white_rook_bin)) if int(white_rook_bin[i])]
    white_knight_squares = [i for i in range(len(white_knight_bin)) if int(white_knight_bin[i])]
    white_bishop_squares = [i for i in range(len(white_bishop_bin)) if int(white_bishop_bin[i])]
    white_queen_squares = [i for i in range(len(white_queen_bin)) if int(white_queen_bin[i])]
    white_king_square = [i for i in range(len(white_king_bin)) if int(white_king_bin[i])]

    fen_dict = {i: None for i in range(64)}

    for s in black_pawn_squares:
        fen_dict[s] = 'p'
    for s in black_rook_squares:
        fen_dict[s] = 'r'
    for s in black_knight_squares:
        fen_dict[s] = 'n'
    for s in black_bishop_squares:
        fen_dict[s] = 'b'
    for s in black_queen_squares:
        fen_dict[s] = 'q'
    for s in black_king_square:
        fen_dict[s] = 'k'
    for s in white_pawn_squares:
        fen_dict[s] = 'P'
    for s in white_rook_squares:
        fen_dict[s] = 'R'
    for s in white_knight_squares:
        fen_dict[s] = 'N'
    for s in white_bishop_squares:
        fen_dict[s] = 'B'
    for s in white_queen_squares:
        fen_dict[s] = 'Q'
    for s in white_king_square:
        fen_dict[s] = 'K'

    fen = ''
    empty = 0
    row = ''
    
    for k, v in fen_dict.items():
        if not k % 8 and not k == 0:
            if empty:
                row += str(empty)
                empty = 0
            fen = row[::-1] + "/" + fen
            row = ''

        if not v:
            empty += 1
            continue

        if empty:
            row += str(empty)
            empty = 0

        row += v[::-1]

    fen = row[::-1] + "/" + fen
    fen = fen.rstrip('/')
        
    
    

    side_to_move_map = {
        Color.WHITE: 'w',
        Color.BLACK: 'b'
    }

    fen += f" {side_to_move_map[board.color_to_move]}"

    w_castle_king = board.castle_rights[Color.WHITE][0] == True
    w_castle_queen = board.castle_rights[Color.WHITE][1] == True
    b_castle_king = board.castle_rights[Color.BLACK][0] == True
    b_castle_queen = board.castle_rights[Color.BLACK][1] == True

    fen += " "

    if w_castle_king:
        fen += "K"
    if w_castle_queen:
        fen += "Q"
    if b_castle_king:
        fen += "k"
    if b_castle_queen:
        fen += "q"

    if not w_castle_king and not w_castle_queen and not b_castle_king and not b_castle_queen:
        fen += "-"

    fen += " "

    if board.en_passant_target:
        fen += str(square_map[board.en_passant_target])
    else:
        fen += "-"

    # Halfmove clock
    fen += f" {str(0)}"

    # Full-move Number
    fen += f" {str(0)}"

    return fen



