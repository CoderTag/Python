number = int(input('Enter length of fibonacci sequence: '))
print(f'you have enter the number: {number}')

def fibo(num=1):
    if num == 1 or num == 2:
        return(num - 1)
    else:
        sum = fibo(num - 2) + fibo(num - 1)
        return(sum)


for i in range(number):
    print(fibo(i + 1), end=" ")

print("\n One more option")


a, b = 0, 1
for i in range(number):
    print(a, end=' ')
    a, b = b, a + b
print("\n")
