
# from T24 import mn
import T24
a = 10

# globals()

# dir()

# locals()


def x():
    global a
    b = 5
    a = a + 2
    print(a)

    def y():
        print(b)
    y()


# def y():
#     print(b)


x()
# T24.mn()
