import sys
sys.path.append('..')
from Engine import *
from multiprocessing import Queue

def test_Engine_set_position(args):
    queue=Queue()
    engine=Engine(queue)
    engine.position(args)
    engine.board.print_board()


def test_Engine_uci_new_game():
    queue=Queue()
    engine=Engine(queue)
    engine.ucinewgame()
    engine.board.print_board()

def test_Engine_go(args):
    queue=Queue()
    engine=Engine(queue)
    engine.position(['startpos'])
    engine.go(args)


test_Engine_go(['depth','3'])



