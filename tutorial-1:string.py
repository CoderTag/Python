msg = """Hello I am here waitng for you...
    When are you coming back? """
print(msg)
msg = "Hello I am here waitng for you. Yes I am"

print(f'length of charecters in the string is : {len(msg)}')
print(msg[2])
print(msg[0:5]) #its call slicing
print(msg[:5])
print(msg[5:])
print('#'*100)
print (msg.lower())
print('#'*100)
print (msg.upper())
print('#'*100)
print (msg.title())
print('#'*100)
print (msg.count('I am'))
print (msg.count('a'))
print (msg.count('z'))
print (msg.count('We are'))
print('#'*100)
new_msg = msg.replace('Hello',"Hey There")
print(new_msg)
print(msg)
print('#'*100)
print(dir(msg))   # show all methods available for the string variable
print('#'*100)
print(help(str))    # details about all methods available to string variable. Here we give variable name wont work. have to provide str itself

