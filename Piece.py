class Piece:
    EMPTY = 0

    wP = 1
    wR = 2
    wN = 3
    wB = 4
    wQ = 5
    wK = 6

    bP = 7
    bR = 8
    bN = 9
    bB = 10
    bQ = 11
    bK = 12

    promoted_pieces={
        0:'',1:'P',2:'R',3:'N',4:'B',5:'Q',6:'K'
    }
    piece_map = {
            'P': 'white_P',
            'N': 'white_N',
            'B': 'white_B',
            'R': 'white_R',
            'Q': 'white_Q',
            'K': 'white_K',
            'p': 'black_P',
            'n': 'black_N',
            'b': 'black_B',
            'r': 'black_R',
            'q': 'black_Q',
            'k': 'black_K'
        }

    white_pieces = {wP, wR, wN, wB, wQ, wK}
    black_pieces = {bP, bR, bN, bB, bQ, bK}

    PAWN = "pawn"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"
