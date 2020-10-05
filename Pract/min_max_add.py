arr = [3, 4, 5, 1, 6]

l = len(arr)
minsum = 0
maxsum = 0
i = 1
while(l):
    if(i != 5):
        minsum = minsum + min(arr)

    if(i != 1):
        maxsum = maxsum + min(arr)
    i = i + 1
    l = l - 1
    arr.remove(min(arr))

print(f'{minsum}   {maxsum}')
