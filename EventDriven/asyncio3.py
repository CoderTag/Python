#!/usr/bin/env python3
# rand.py

import asyncio
import random
from colorama import Fore
import time


async def makerandom(idx, threshold=6):
    if idx == 0:
        my_color = Fore.BLUE
    elif idx == 1:
        my_color = Fore.WHITE
    else:
        my_color = Fore.GREEN

    print(my_color + f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(my_color + f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(my_color + f"---> Finished: makerandom({idx}) == {i}" + Fore.MAGENTA)
    d = {"name": "kanisq", "age": 20}
    l = [1, 2, 3]
    t = (20, 21)
    return i, i, d, l, t
    # return i


async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    print(Fore.RED, res)
    return res

if __name__ == "__main__":
    random.seed(4444)
    s = time.perf_counter()
    loop = asyncio.get_event_loop()
    r1, r2, r3 = loop.run_until_complete(main())

    # r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}\n, r2: {r2}\n, r3: {r3}\n")
    loop.close()

    print(Fore.GREEN + f"Time : {time.perf_counter() - s}")
