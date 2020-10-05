

def add_decorator(funcName):
    v = 10

    def funcName(a, b):
        print(a + b + 10)
    return funcName


# add = add_decorator(add)
@add_decorator
def add(a, b):
    print(a + b)


add(4, 5)
