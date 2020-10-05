courses = ["Math", "Physics","Chemistry"]
courses_2 = ["History","Geography"]
courses.append("Art")
print(courses)
courses.insert(3,"Biology")
print(courses)

courses.insert(0,courses_2)
print(courses)  # It insert the second list itself not individual value
courses = ["Math", "Physics","Chemistry"]
courses_2 = ["History","Geography"]
courses.extend(courses_2)
print(courses)
courses.remove('Chemistry')
print(courses)
popped = courses.pop()       # remove last element
print(f'{popped} popped and list is now {courses}')
courses.reverse()
print(courses)
courses.sort()
print(courses)

nums = [43,2,53,1,75]
nums.sort(reverse=True) # it will sort and then reverse in place
print(nums)

# We can also sort our list without sorting the original list
nums = [43,2,53,1,75]
new_nums = sorted(nums)
print(f'{nums} and {new_nums}')
print(sum(nums))        # summation of all elements
print(courses.index('Math'))        # print index of an element
print('Art' in courses)     # check value is in list

for item in courses:
    print(item)

for index,item in enumerate(courses, start=1):
    print(index,': ',item)

courses_str = ', '.join(courses)
print(courses_str)
courses_new = courses_str.split(', ')
print(courses_new)
