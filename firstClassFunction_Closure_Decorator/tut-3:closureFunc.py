# So what are closures good for?

# Closures can avoid the use of global values and provides some form of data hiding.
# It can also provide an object oriented solution to the problem.

# When there are few methods (one method in most cases) to be implemented in a class,
# closures can provide an alternate and more elegant solutions. But when the number of attributes and methods get larger,
# better implement a class.


import logging

logging.basicConfig(filename="example.log", level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(f'function {func.__name__} is called with arguments {args}')
        print(func(*args))
    return log_func


def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


def multiply(*args):
    prod = 1
    for arg in args:
        prod *= arg
    return prod


add = logger(add)
prod = logger(multiply)

add(1, 2, 3, 4, 5)
prod(1, 2, 3, 4)
