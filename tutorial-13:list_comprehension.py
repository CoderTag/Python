count = int(input("How many number you want to enter: "))
i = 1
my_list = list()
while(count > 0):
    num = int(input(f'Input {i} number: '))
    my_list.append(num)
    i += 1
    count -= 1

print(f'List is: {my_list}')
print("Convert list to binary.. if even than 0 else 1")

#List Comprehensions
bin_list = [0 if i%2 == 0 else 1 for i in my_list]
print(bin_list)

#Find Even number
number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

#nested if
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)



