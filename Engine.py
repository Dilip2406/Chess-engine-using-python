from multiprocessing import Event,Queue
from Board import *
from Move import *
from evaluate import *
from movegen import *
from time import time
from random import choice

class Engine:
    def __init__(self, queue:Queue):
        self.queue = queue
        self.board = Board()
        self.nodes=0
        self.best_move=None

    def start(self):
        while True:
            command = self.queue.get()
            if command=="quit":
                break
            elif command=="stop":
                continue

    def uci_loop(self):
        while True:
            full_command = input().strip().split()
            if not full_command:
                continue
            command = full_command[0]
            args = full_command[1:]

            match command:
                case "uci": self.uci(),
                case "isready": print("readyok"),
                case "go": self.go(args),
                case "stop": self.stop(),
                case "ucinewgame": self.ucinewgame(),
                case "position": self.position(args),
                case "quit":
                    quit()
                    break
                case _: continue
    def uci(self):
        print("id name Chess-engine-using-python")
        print("id author Dilip and Bharat")
        print("uciok")

    def ucinewgame(self):
        self.board=Board()
        
    def position(self,args):
        if args[0]=="startpos":
            self.board=Board()
            self.board.initialize_board()
            if len(args)>1 and args[1]=="moves":
                for move in args[2:]:
                    user_move=Move.encode_move(square_indices[move[0:2]],square_indices[move[2:4]],0,0)
                    Move.print_move(user_move)
                    self.board=self.board.make_move(Move,user_move)

        if args[0]=="fen":
            self.board.update_from_fen(args[1:])

    def go(self,args):
        self.search(self.board,3)
    def quit(self):
        self.queue.put("quit")
    def stop(self):
        self.queue.put("stop")

    def search(self, board: Board, max_depth: float) -> None:
        moves_list=generate_moves(board)
        self.best_move= choice(moves_list)
        depth = 0
        search_started = time() - 0.0001
        self.nodes=0

        while depth < max_depth:
            depth += 1
            try:
                evaluation = self.negamax(board, depth)
            except RuntimeError:
                break

            current_time = time() - search_started
            
            print(f"info depth {depth} score cp {evaluation} "
                  f"nodes {self.nodes} nps {int(self.nodes / current_time)} ",flush=True)
            
        Move.print_move(self.best_move)

    def negamax(self,board:Board,depth):
        self.nodes+=1
        if depth==0:
            return evaluate(board)
        
        best_score=float('-inf')
        for move in generate_moves(board):
            new_board=board.make_move(Move,move)
            if new_board is None:
                continue
            score=self.negamax(new_board,depth-1)
            if score > best_score:
                best_score = score
                self.best_move = move
        return best_score


