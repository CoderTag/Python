from collections import defaultdict
colors = ['red', 'green', 'blue', 'green', 'blue', 'green', 'blue', 'red', 'green']

d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print(d)
print('<->' * 20)

d = {}
for color in colors:
    d[color] = d.get(color, 0 + 1)
print(d)
print('<->' * 20)

d = defaultdict(int)
for color in colors:
    d[color] += 1
print(d)
print(dict(d))
print('<->' * 20)

ice_cream = defaultdict(lambda: 'Vanilla')
ice_cream['Sarah'] = 'Chunky Monkey'
ice_cream['Abdul'] = 'Butter Pecan'
print(ice_cream['Sarah'])
print(ice_cream['Joe'])
