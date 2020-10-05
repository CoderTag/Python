names = ['nilu', 'pilu', 'tilu']
colors = ['red', 'green', 'blue']
songs = ['Tere', 'Mere', 'Milan']

for color in sorted(colors):
    print(color)

print("*" * 100)
for color in sorted(colors, reverse=True):
    print(color)

print("*" * 100)
print("custom sort")


def compare_length(c1, c2):
    if len(c1) < len(c2):
        return -1
    if len(c1) < len(c2):
        return 1
    return 0


print(sorted(colors, key=len))
