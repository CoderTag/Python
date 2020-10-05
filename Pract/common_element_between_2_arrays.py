a = [1, 2, 3, 4, 5, 6]
b = [3, 4, 5, 6, 7, 8]

# Option-1

# for i in a:
#     if i in b:
#         print("yes--->{}".format(i))
#     else:
#         print("no--->{}".format(i))

# Option-2
# for i in a:
#     for j in b:
#         if i < j:
#             break
#         elif i == j:
#             print("Yes--->{}".format(i))
#             break
#         else:
#             continue

# Option-3
a = set(a)
b = set(b)

if a & b:
    print(a & b)
else:
    print("No Match")

# Option-4
if len(a.intersection(b)) > 0:
    print(a.intersection(b))
else:
    print("No Match")
