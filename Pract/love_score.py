name1 = input("first name:")
name2 = input("2nd name:")
name = name1.lower() + name2.lower()
t = 0
l = 0
for n in name:
    if n in ("True".lower()):
        t += 1
    if n in ("Love".lower()):
        l += 1
print(str(t) + str(l))