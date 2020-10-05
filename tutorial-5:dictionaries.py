student = {'name':'Kas', 'age':40, 'courses':['AI','ML']}
print(student)
print(student['name'])

#print(student['phone']) # it will error out as the key doesnot exist
print(student.get('phone')) # instead of error out it will return None
print(student.get('phone','Not Found')) #can also specify default value if the key doesnot exist

student['name'] = "Bunt"
student['phone'] = '55-33-343'
print(student)

# we can also update the dictionary in one shot
student = {'name':'Kas', 'age':40, 'courses':['AI','ML']}
student.update({'name':'Bunty','phone':'22-3232-32'})
print(student)

del student['age']
print(student)

# we can also delete a value from dictionary using pop method and capture the deleted value
phone = student.pop('phone')
print(student)
print(phone)

print(len(student)) # numebr of keys
print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
    print(key,':',value)
