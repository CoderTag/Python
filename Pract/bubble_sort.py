import re

# p = re.compile(r'^[0-9]+')
# arr = []
# while True:
#     ar = input("Enter a list of number or type anything else apart from number to once you are done: ")
#     if p.search(ar):
#         arr.append(int(ar))
#     else:
#         break

# if arr:
#     print(arr)

arr = [5, 4, 3, 2, 1]
arr_len = len(arr)

for j in range(arr_len):
    # print(f'J : {j}  and {arr[j]}')
    count = j + 1
    for i in range(count, arr_len):
        if arr[i] <= arr[j]:
            (arr[j], arr[i]) = (arr[i], arr[j])
            print(f"j:{j} - i:{i} : {arr}")
        else:
            continue
