import json

with open('state.json') as f:
    data = json.load(f)
# print(data)

for stat in data['states']:
    print(stat)
    del stat['area_codes']

with open('new_state.json', 'w') as f:
    json.dump(data, f, indent=2)
