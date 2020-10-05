courses = ('Math','Physics','Chemistry')
course2 = courses

print(courses)
print(course2)

# Tuple is immutable so follwoing line will throw error
#courses[0] = "Art"
print('#'*100)

#set are values of unordered and also throw away duplicate

cs_courses = {'Math','Physics','Chemistry','Math','English'}
art_courses = {'Math','Art','Design','English'}
print(cs_courses)

# Membership test set does more efficiently that list or tuples
# check if member is part of set or not
print('Math' in cs_courses)    # list and tuple can do the same for set are optimized for this

# it check which values are shared or not shared with other set
print(cs_courses.intersection(art_courses))
courses = cs_courses.intersection(art_courses)
print(courses)

print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

