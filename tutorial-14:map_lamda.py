# The syntax of map() is:
# map(function, iterable, ...)

def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)
print('#'*100)

#use lambda function with map()
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

numbersSquare = list(result)
print(numbersSquare)

#Multiple Iterators to map() Using Lambda
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))
