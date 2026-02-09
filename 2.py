print("\033c")

import threading
from datetime import datetime
import random
import time

lock = threading.Lock()
tickets = 10

def cell(name):
    global tickets
    while True:
        with lock:
            if tickets <= 0:
                return
            tickets -= 1
            current = tickets
        
        time.sleep(random.uniform(0.01, 0.1))
        print(f"{name} -1 ticket. Tickets: {current}")

threads = [threading.Thread(target = cell, args = (i,)) for i in range(5)]

start = datetime.now()

for t in threads: t.start()
for t in threads: t.join()

print(f"Tickets: {tickets}, Time: {datetime.now() - start}")