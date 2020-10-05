try:
    f = open("test.txt")
   # bdf = refitfd
except FileNotFoundError as e:
    print(e)

except Exception as e:  # this is very generic exception
    print(e)

else:           # it will hit if try block does not raise exception
    print(f.read())
    f.close()
finally:
    print("Run always irrespective of exception occur or not")


# Developer can raise their own exception
try:
    f = open("test.txt")
    if f.name == 'test.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Self defined Exceptions")
