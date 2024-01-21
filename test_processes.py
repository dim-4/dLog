
from random import random
from time import sleep
# multiprocessing
from multiprocessing import Process, Lock
from dlog import *

def bar(lock, process_id):
    filename = f'./test_data/{l.logger_uid}.log'
    l(f"Process {process_id} started ! Logger id: {l.logger_uid}.", 
      color = [RED, GRN, BLU][process_id%3], lock=lock, filename=filename)
    sleep(0.4)
    l(f"Process {process_id} done !", color = [RED, GRN, BLU][process_id%3], 
      lock=lock, filename=filename)

lock = Lock()
l = Logger(prepend_logger_uid_to_filename=True)

if __name__ == "__main__":

    processes = [Process(target=bar, args=(lock, i, )) for i in range(10)]
    for p in processes:
        p.start()

    for i in range(15):
        print(i)
        sleep(0.01)

    for p in processes:
        p.join()

    print(l.log_count)

