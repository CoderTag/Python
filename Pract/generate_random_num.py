import random


def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


# Driver Code
num = 100
start = 0
end = 100000
l = Rand(start, end, num)
print(l)
l2 = set(l)

if 80000 in l:
    pass
else:
    print("h")
