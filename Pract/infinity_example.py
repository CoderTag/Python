a = [43, 5643, 12, 2, 45]

smallest = float("inf")

for num in a:
    if num < smallest:
        smallest = num

print(smallest)

# Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number
# of consecutive 's in 's binary representation.
n = 951  # try with n = 45353 n=35325 many other integer
b = format(n, 'b')
print(b)
b += '0'
print(b)

max = float("-inf")

count = 0
for s in b:
    if s == '1':
        count += 1
        continue
    elif count > max:
        max = count
    count = 0
print(max)
