score = [2, 4, 5, 6, 7]
# get first and last number
a, b, c, d, e = score
print(a, e)

# average of score except the last one
*s, l = score
print(sum(s) / len(s))

# average of score except the last and first one
f, *s, l = score
print(sum(s) // len(s))
print("#" * 50)
studsDb = [
    ("class-III", "acacia", 9),
    ("class-III", "veena", 9),
    ("class-VI", "kanishq", 12),
    ("class-VI", "tanmay", 12),
    ("class-VI", "vivan", 12),
    ("class-VI", "tanu", 9),
    ("class-III", "paklyu", 9),
]

VI, III = [], []

for i in studsDb:
    cls, name, _ = i
    if cls == "class-III":
        III.append(name)
    if cls == "class-VI":
        VI.append(name)

print(III)
print(VI)
print("#" * 50)
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)
