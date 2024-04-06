from multiprocessing import Process, Queue
from Engine import *
from time import sleep

def main() -> None:
    print(f"Chess-engine-using-python 1.0 by Dilip and Bharat")

    queue = Queue()
    Process(target=Engine(queue).start, daemon=True).start()
    sleep(0.1)  

    Engine(queue).uci_loop()


if __name__ == "__main__":
    main()
