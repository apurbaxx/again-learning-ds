"""
MultiProcessing is used for CPU bound tasks
Senario: Factorial Calculation
factorial calculation, especially for large numbers,
involve singnificant computational work. Multiprocessing
can be used to distribute the workload across multiple
CPU cores, imporving performance.
"""

import math
import multiprocessing
import sys
import time

# Increase the maximum number of digiys for Integer conversion

sys.set_int_max_str_digits(100000)

##Function to compute factorials of a given number


def compute_factorials(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result


if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000]
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorials, numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")
