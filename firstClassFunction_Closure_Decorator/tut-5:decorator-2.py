import functools

# Decorating Functions With Arguments and without argument

#following is the complete template of a decorator
def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_do_twice


@do_twice
def say_whee():
    print("Whee!")


say_whee()


@do_twice
def say_intro(name):
    print(f"My name is {name}")


say_intro("Pakul")

# Returning Values From Decorated Functions


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


adam = return_greeting("Ballu")
print(adam)


# run folling two line after commenting @functools.wraps(func) line in do_twice decorator.
# compare output. When you comment function has gotten very confused about its identity.
# it will consider wrapper as it's identity
print(return_greeting.__name__)
print(help(return_greeting))


# Ref : https://realpython.com/primer-on-python-decorators/
