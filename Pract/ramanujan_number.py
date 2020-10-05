from collections import defaultdict
import math
n = 1000000
qubes = [y**3 for y in range(int(n**(1 / 3)) + 1)]
ramanujan = defaultdict(int)
mnumbers = defaultdict(list)

for ind, a in enumerate(qubes):
    for b in qubes[ind:]:
        if a + b > n:
            break
        ramanujan[a + b] += 1
        mnumbers[a + b].extend([a, b])

ramj_nums = sorted(n for n in ramanujan if ramanujan[n] == 2)
print(ramj_nums)

# l = [1729]
for i in ramj_nums:
    li = len(mnumbers[i])
    lcount = 0
    rcount = 1
    while(li):
        a = math.ceil(mnumbers[i][lcount]**(1 / 3))
        b = math.ceil(mnumbers[i][rcount]**(1 / 3))
        print(f'{a}^3 + {b}^3 = {i}')
        li -= 2
        lcount += 2
        rcount += 2
