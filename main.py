import math
import multiprocessing as mp
import time


def cpu_load_task():
    while True:
        _ = math.sqrt(64*64*64*64*64*64*64)


TIMEOUT = 180


if __name__ == '__main__':
    pool = mp.Pool()
    results = [pool.apply_async(cpu_load_task) for _ in range(32)]
    time.sleep(TIMEOUT)
    pool.terminate()
