import json
import re
with open('t.json') as f:
    data = json.load(f)

# print(type(data['fields']))

choices = []
for f in data['fields']:
    prop = {}
    if 'properties' not in f.keys():
        continue
    prop = f['properties']
    if 'choices' not in prop.keys():
        continue
    # print(prop['choices'])
    choices.extend(prop['choices'])


# Remove id,attachment keys from all choices
my_keys = ['id', 'attachment']
# for choice in choices:
#     for mk in list(choice.keys()):
#         if mk in my_keys:
#             del choice[mk]
#             continue

# 2nd way of removing keys in one line
new_choices = []
for choice in choices:
    if not re.search(r'Z\d|Y\d|X\d|kW\)', choice['label']):
        # choice.clear()
        continue
    list(map(choice.__delitem__, filter(choice.__contains__, my_keys)))
    new_choices.append(choice)

label_occurance = {}
for choice in new_choices:
    print(choice)
    try:
        label_occurance[choice['label']].append(choice['ref'])
    except:
        label_occurance[choice['label']] = []
        label_occurance[choice['label']].append(choice['ref'])

for k, v in label_occurance.items():
    print(k, " ==> ", v)
    print(f'length: {len(v)}')

# print(label_occurance)
