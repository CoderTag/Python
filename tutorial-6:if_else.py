#difference between == and is

a = [1,2,3]
b = [1,2,3]
c = a
print(f'address of object a: {id(a)}')
print(f'address of object b: {id(b)}')
print(f'address of object c: {id(c)}')

if a == b:
    print("Both arrays are having same value")

if a == c:
    print("Both arrays are having same value")

if a is b:
    print("Both arrays are having different address location")

if a is c:
    print("Both arrays are having same address location")

