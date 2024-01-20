
from random import random
from time import sleep
from threading import Thread
from dlog import *

l = Logger()

def foo(thread_id):
    if random() > 0.5:
        sleep(random())
    l(f"Thread {i} started !", color = [RED, GRN, BLU][i%3])


threads = [Thread(target=foo, args=(i,)) for i in range(100)]
for t in threads:
    t.start()
    t.join()
