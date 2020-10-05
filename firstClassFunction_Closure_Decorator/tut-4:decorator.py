# Example-1
# ==========


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)
print(say_whee)
print("Refer to func: ", say_whee.__name__)
say_whee()

# Example-2
# ==========
# Put simply: decorators wrap a function, modifying its behavior.
from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper


def say_whee():
    print("Whee!")


say_whee = not_during_the_night(say_whee)

# Example-3
# ==========
# The way you decorated say_whee() above is a little clunky. First of all, you end up typing the name say_whee three times.
# Python allows you to use decorators in a simpler way with the @ symbol sometimes called the “pie” syntax


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")
