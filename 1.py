import time
import threading
import os
from datetime import datetime
import dis

print("\033c")

def func_sleep():
    print(f"Thread {threading.get_ident()} | process {os.getpid()}")
    time.sleep(1)

# start = datetime.now()
# for _ in range(3):
#     func_sleep()
# print(f"Total 1: {datetime.now() - start}")

def func_math():
    cnt = 0
    for _ in range(30_000_000):
        cnt += 1
    print(f"Thread {threading.get_ident()} | process {os.getpid()}")

# start = datetime.now()
# for _ in range(3):
#     func_math()
# print(f"Total 2: {datetime.now() - start}")

cnt = 0
def func_inc():
    global cnt
    for _ in range(10):
        cnt += 1
        print(f"Threaf {threading.get_ident()} | cnt {cnt}")

def func_mix():
    cnt = 0
    for _ in range(5):
        cnt += 1
        print(f"Threaf {threading.get_ident()} | cnt {cnt}")

    time.sleep(1)
    return cnt



start = datetime.now()

th1 = threading.Thread(target = func_mix, daemon = True)
th2 = threading.Thread(target = func_mix, daemon = True)
th3 = threading.Thread(target = func_mix, daemon = True)

th1.start()
th2.start()
th3.start()

# th1.join()
# th2.join()
# th3.join()

print(f"Total 2: {datetime.now() - start}")
