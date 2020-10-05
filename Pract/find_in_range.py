# Find all prime numbers in the given range
import math
start = 0
end = 1000000
sqrt_num = math.sqrt(end)
ceil_num = math.ceil(sqrt_num)

for num in range(start, end + 1):
    is_prime = True
    if (num == 1) or(num == 0):
        continue
    if num == 2:
        print(num, end=" ")
        continue

    if num < ceil_num:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    else:
        for r in range(2, ceil_num + 1):
            if num % r == 0:
                is_prime = False
                break

    # if is_prime:
    #     print(num, end=" ")

print()
