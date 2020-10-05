# Find the number is prime or not

import math
import sys

num = 100
sqrt_num = math.sqrt(num)
int_num = int(sqrt_num)
ceil_num = math.ceil(sqrt_num)

if ceil_num == int_num:
    print("Not a Prime number. Perfect Square")
else:
    for r in range(2, ceil_num + 1):
        if num % r == 0:
            print("Not a Prime number")
            break
    else:
        print("Prime number")
