def square(x):
    return x * x


# This is what we generally do store the return value of a func to a variable
f1 = square(5)
print(square)
print(f1)

# in fist class we store func address. Don;t give parentheis. Parenthesis with a func name means we want to execute it
f = square
print(square)
print(f)

# LEts write our own map function


def my_map(func_name, args):
    result = []
    for i in args:
        result.append(func_name(i))
    return result


nums = [1, 2, 3, 4]
r = my_map(square, nums)
print(r)
