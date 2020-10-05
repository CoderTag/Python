# Create a @timer decorator. It will measure the time a function takes to execute and print the duration to the console.

import functools
import time


def timer(func):
    functools.wraps(func)

    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        run_time = time.perf_counter() - start_time
        print(f"finish {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        print(sum(i**2 for i in range(1000)))


waste_some_time(10)
