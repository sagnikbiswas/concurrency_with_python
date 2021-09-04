"""
Python script to **synchronously** do some CPU bound calculations with a single CPU core.
Check the .ipynb file for details.
"""

import multiprocessing
import time


def cpu_bound(number):
    name = multiprocessing.current_process().name
    print(f"{name} is crunching numbers")
    return sum(i * i for i in range(number))


def find_sums(numbers):
    with multiprocessing.Pool(processes=8) as pool:
        pool.map(cpu_bound, numbers)


if __name__ == "__main__":
    numbers = [10_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")