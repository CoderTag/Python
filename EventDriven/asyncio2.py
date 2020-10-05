import asyncio
import time
from colorama import Fore


async def abc():
    for i in range(20):

        if i % 10 == 0:
            await asyncio.sleep(1)
            print(Fore.BLUE + "abc")


async def xyz():
    for i in range(20):
        if i % 10 == 0:
            await asyncio.sleep(1)
            print(Fore.WHITE + "xyz")


async def main():

    await asyncio.gather(abc(), xyz())


if __name__ == "__main__":
    s = time.perf_counter()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
    elapsed = time.perf_counter() - s
    print(Fore.GREEN + f"{__file__} executed in {elapsed:0.2f} seconds.")
