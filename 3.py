from datetime import datetime
import threading
import multiprocessing as mp
import time
import os

def server(i, COUNT, io_delay):
    time.sleep(io_delay)
    grs = (i * COUNT, i * COUNT + COUNT)
    return grs

def count_single(g1, g2):
    count = 0
    for x in range(g1, g2):
        if is_simple(x):
            count += 1
    return count

def is_simple(x):
    if x < 2:
        return False
    elif x % 2 == 0:
        return x == 2
    
    for d in range(3, int(x**0.5)+1, 2):
        if x % d == 0:
            return False
    return True

def run_single(COUNT, n_workers, io_delay):
    start = datetime.now()
    total = 0
    for i in range(n_workers):
        g1, g2 = server(i, COUNT, io_delay)
        total += count_single(g1, g2)
    end = datetime.now() - start
    return total, end

def run_thread(COUNT, n_workers, io_delay):
    result = [0] * n_workers

    def worker(i):
        g1, g2 = server(i, COUNT, io_delay)
        result[i] = count_single(g1, g2)

    threads = []
    start = datetime.now()

    for i in range(n_workers):
        th = threading.Thread(target = worker, args = (i, ))
        th.start()
        threads.append(th)

    for t in threads:
        t.join()

    total = sum(result)
    end = datetime.now() - start

    return total, end


def main():
    COUNT = 50_000
    n_workers = 8
    io_delay = 0.5

    s_total, s_time = run_single(COUNT, n_workers, io_delay)
    print(f"Single: {s_total} - {s_time}")

    t_total, t_time = run_thread(COUNT, n_workers, io_delay)
    print(f"Thread: {t_total} - {t_time}")

if __name__ == "__main__":
    main()
