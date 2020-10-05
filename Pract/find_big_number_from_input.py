count = int(input("How many number you want to enter: "))
i = 1
my_list = list()
while(count > 0):
    num = int(input(f'Input {i} number: '))
    my_list.append(num)
    i += 1
    count -= 1

print(f'Biggest number entered by you is : {max(my_list)}')
print(f'Smallest number entered by you is : {min(my_list)}')
