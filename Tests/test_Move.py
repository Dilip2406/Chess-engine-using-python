import sys
sys.path.append('..')
from Move import *

'''
square_indices = {
    'a8': 0,  'b8': 1,  'c8': 2,  'd8': 3,  'e8': 4,  'f8': 5,  'g8': 6,  'h8': 7,
    'a7': 8,  'b7': 9,  'c7': 10, 'd7': 11, 'e7': 12, 'f7': 13, 'g7': 14, 'h7': 15,
    'a6': 16, 'b6': 17, 'c6': 18, 'd6': 19, 'e6': 20, 'f6': 21, 'g6': 22, 'h6': 23,
    'a5': 24, 'b5': 25, 'c5': 26, 'd5': 27, 'e5': 28, 'f5': 29, 'g5': 30, 'h5': 31,
    'a4': 32, 'b4': 33, 'c4': 34, 'd4': 35, 'e4': 36, 'f4': 37, 'g4': 38, 'h4': 39,
    'a3': 40, 'b3': 41, 'c3': 42, 'd3': 43, 'e3': 44, 'f3': 45, 'g3': 46, 'h3': 47,
    'a2': 48, 'b2': 49, 'c2': 50, 'd2': 51, 'e2': 52, 'f2': 53, 'g2': 54, 'h2': 55,
    'a1': 56, 'b1': 57, 'c1': 58, 'd1': 59, 'e1': 60, 'f1': 61, 'g1': 62, 'h1': 63,
}
'''

def get_move_src():
    #Test 1 :Check whether the source square is getting returned correctly
    move=Move.encode_move(square_indices['e2'],square_indices['e4'],0,0)
    assert Move.get_move_src(move)==52
    print("Passed Test 1")
    

def get_move_dest():
    #Test 2 :Check whether the destination square is getting returned correctly
    move=Move.encode_move(square_indices['e2'],square_indices['e4'],0,0)
    assert Move.get_move_dest(move)==36
    print("Passed Test 2")
    

def encode_move():
    #Test 3 :Check whether the move is getting encoded correctly
    move=Move.encode_move(1,1,0,0)
    ans=0b1000001
    np.uint32(ans)
    assert move==ans
    print("Passed Test 3")
    

get_move_dest()