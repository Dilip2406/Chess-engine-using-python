import numpy as np

def set_bit(bitboard, square):
        return bitboard | (np.uint64(1) << np.uint64(square))

def pop_bit(bitboard, square):
    return bitboard & ~(np.uint64(1) << np.uint64(square))

def pop_lsb(bitboard):
    return bitboard & (bitboard - np.uint64(1))

def print_bitboard(bitboard):
    print("")
    for rank in range(8):
        for file in range(8):
            square= rank *8 +file
            if not file :
                print(8-rank,end="")
                print("   ",end="")
            print(1 if get_bit(bitboard,square) else 0,end="")
            print(" ",end="")
        print("")
    print("\n    a b c d e f g h \n\n")

def get_bit(bitboard,square):
    return (bitboard >> np.uint64(square)) & np.uint64(1)

def get_lsb(bitboard):
    board=int(bitboard)
    if(board==0):
        return -1
    return count_bits(np.uint64((board & -board)-1))

def count_bits(bitboard):
    count=0
    while bitboard:
        count+=1
        bitboard&=bitboard-np.uint64(1)
    return count



'''
      ATTACK PATTERNS

'''
def get_pawn_attacks(square, color):
    attacks = np.uint64(0)
    if color == 'black':
        if (square % 8) > 0:
            attacks = set_bit(attacks, square + 7)
        if (square % 8) < 7:
            attacks = set_bit(attacks, square + 9)
    else:
        if (square % 8) > 0:
            attacks = set_bit(attacks, square - 9)
        if (square % 8) < 7:
            attacks = set_bit(attacks, square - 7)
    return attacks

def get_pawn_pushes(square, color):
    motion_bb=np.uint64(0)
    if color == 'black':
        motion_bb=set_bit(motion_bb, square + 8)
        if square // 8 == 1:
            motion_bb=set_bit(motion_bb, square + 16)
    else:
        motion_bb=set_bit(motion_bb, square - 8)
        if square // 8 == 6:
            motion_bb=set_bit(motion_bb, square - 16)
    return motion_bb

def get_knight_attacks(square):
    attacks = np.uint64(0)
    if square + 17 < 64 and (square % 8) < 7:
        attacks = set_bit(attacks, square + 17)
    if square + 15 < 64 and (square % 8) > 0:
        attacks = set_bit(attacks, square + 15)
    if square + 10 < 64 and (square % 8) < 6:
        attacks = set_bit(attacks, square + 10)
    if square + 6 < 64 and (square % 8) > 1:
        attacks = set_bit(attacks, square + 6)
    if square - 17 >= 0 and (square % 8) > 0:
        attacks = set_bit(attacks, square - 17)
    if square - 15 >= 0 and (square % 8) < 7:
        attacks = set_bit(attacks, square - 15)
    if square - 10 >= 0 and (square % 8) > 1:
        attacks = set_bit(attacks, square - 10)
    if square - 6 >= 0 and (square % 8) < 6:
        attacks = set_bit(attacks, square - 6)
    return attacks

def get_king_attacks(square):
    attacks = np.uint64(0)
    if square + 8 < 64:
        attacks = set_bit(attacks, square + 8)
    if square - 8 >= 0:
        attacks = set_bit(attacks, square - 8)
    if (square % 8) < 7:
        attacks = set_bit(attacks, square + 1)
        if square + 9 < 64:
            attacks = set_bit(attacks, square + 9)
        if square - 7 >= 0:
            attacks = set_bit(attacks, square - 7)
    if (square % 8) > 0:
        attacks = set_bit(attacks, square - 1)
        if square + 7 < 64:
            attacks = set_bit(attacks, square + 7)
        if square - 9 >= 0:
            attacks = set_bit(attacks, square - 9)
    return attacks

def get_bishop_attacks(square, block):
        # result attacks bitboard
        attacks = np.uint64(0)
        
        # init ranks & files
        r, f = 0, 0
        
        # init target rank & files
        tr = square // 8
        tf = square % 8
        
        # generate bishop attacks
        for r, f in zip(range(tr + 1, 8), range(tf + 1, 8)):
            attacks = set_bit(attacks, r * 8 + f)
            if get_bit(block, r * 8 + f):
                break
        
        for r, f in zip(range(tr - 1, -1, -1), range(tf + 1, 8)):
            attacks = set_bit(attacks, r * 8 + f)
            if get_bit(block, r * 8 + f):
                break
        
        for r, f in zip(range(tr + 1, 8), range(tf - 1, -1, -1)):
            attacks = set_bit(attacks, r * 8 + f)
            if get_bit(block, r * 8 + f):
                break
        
        for r, f in zip(range(tr - 1, -1, -1), range(tf - 1, -1, -1)):
            attacks = set_bit(attacks, r * 8 + f)
            if get_bit(block, r * 8 + f):
                break
        
        # return attack map
        return attacks


def get_rook_attacks(square, block):
    # result attacks bitboard
    attacks = np.uint64(0)
    
    # init ranks & files
    r, f = 0, 0
    
    # init target rank & files
    tr = square // 8
    tf = square % 8
    
    # generate rook attacks
    for r in range(tr + 1, 8):
        attacks = set_bit(attacks, r * 8 + tf)
        if get_bit(block, r * 8 + tf):
            break
    
    for r in range(tr - 1, -1, -1):
        attacks = set_bit(attacks, r * 8 + tf)
        if get_bit(block, r * 8 + tf):
            break
    
    for f in range(tf + 1, 8):
        attacks = set_bit(attacks, tr * 8 + f)
        if get_bit(block, tr * 8 + f):
            break
    
    for f in range(tf - 1, -1, -1):
        attacks = set_bit(attacks, tr * 8 + f)
        if get_bit(block, tr * 8 + f):
            break
    
    # return attack map 
    return attacks



def get_queen_attacks(square, occupied):
    return get_rook_attacks(square, occupied) | get_bishop_attacks(square, occupied)





###block=set_bit(np.uint64(0), 57)
#block=set_bit(block, 49)
#print_bitboard(get_queen_attacks(56,block))









