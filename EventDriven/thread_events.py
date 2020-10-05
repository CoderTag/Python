import threading
import queue
import time
import numpy as np


def flag():
    time.sleep(2)
    event.set()
    print("starting countdown")
    time.sleep(7)
    print("event clear")
    # event.clear()


def start_operation():
    event.wait()
    while event.is_set():
        print("random int")
        event.clear()
        x = np.random.randint(1, 30)
        time.sleep(.5)
        if x == 29:
            print("True")
    print('Event cleared')


event = threading.Event()
t1 = threading.Thread(target=flag)
t2 = threading.Thread(target=start_operation)

t1.start()
t2.start()
