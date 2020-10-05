#https://www.hackerrank.com/challenges/30-2d-arrays/problem
arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]

sum = []
lines = len(arr)
columns = 0
if lines:
    columns = len(arr[0])

# if lines < 3 > columns:
#     print('can not create hour glass')


# for i in range(lines - 2):
#     j = 0
#     s = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
#     sum.append(s)
#     s = arr[i][j + 1] + arr[i][j + 2] + arr[i][j + 3] + arr[i + 1][j + 2] + arr[i + 2][j + 1] + arr[i + 2][j + 2] + arr[i + 2][j + 3]
#     sum.append(s)
#     s = arr[i][j + 2] + arr[i][j + 3] + arr[i][j + 4] + arr[i + 1][j + 3] + arr[i + 2][j + 2] + arr[i + 2][j + 3] + arr[i + 2][j + 4]
#     sum.append(s)
#     s = arr[i][j + 3] + arr[i][j + 4] + arr[i][j + 5] + arr[i + 1][j + 4] + arr[i + 2][j + 3] + arr[i + 2][j + 4] + arr[i + 2][j + 5]
#     sum.append(s)

for i in range(lines - 2):
    for j in range(4):
        s = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
        sum.append(s)

print(max(sum))
