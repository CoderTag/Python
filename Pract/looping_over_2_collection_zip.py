# ignore this
names = ['nilu', 'pilu', 'tilu']
colors = ['red', 'green', 'blue']
songs = ['Tere', 'Mere', 'Milan']

n = min(len(names), len(colors))

for i in range(n):
    print(names[i], '-->', colors[i])

# rather do this

for name, color, song in zip(names, colors, songs):
    print(name, '-->', color, '-->', song)

li = list(zip(names, colors))
print(li)

dict1 = dict(zip(names, colors))
print(dict1)
