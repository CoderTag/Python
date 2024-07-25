# check if a number is prime or not
import math


def prime(num):
    sqrt_num = round(math.sqrt(num))
    is_prime = 1
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            is_prime = 0
            break
    if (is_prime):
        print("Prime")
    else:
        print('Not a Prime')


prime(14)
