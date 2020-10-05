num1 = 10
num2 = 10

print("address of num1 : {}".format(id(num1)))
print("address of num2 : {}".format(id(num2)))
if num1 == num2:
    print("Equal")
if num1 is num2:
    print("Equal Again")

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("address of a : {}".format(id(a)))
print("address of b : {}".format(id(b)))
print("address of c : {}".format(id(c)))

if a == b:
    print("a & b Equal")
else:
    print("a & b not Equal")

if a is b:
    print("a & b identical")
else:
    print("a & b not identical")


if a == c:
    print("a & c Equal")
else:
    print("a & c not Equal")

if a is c:
    print("a & c identical")
else:
    print("a & c not identical")
