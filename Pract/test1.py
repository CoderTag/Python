# str = '''
# {{
#                     "action": "add",
#                     "details": {{
#                         "target": {{
#                             "type": "variable",
#                             "value": "score"
#                         }},
#                         "value": {{
#                             "type": "constant",
#                             "value": {0}
#                         }}
#                     }},
#                     "condition": {{
#                         "op": "is",
#                         "vars": [
#                             {{
#                                 "type": "field",
#                                 "value": "1c1e048b-4cc1-46ff-bdf8-6b0e32a515be"
#                             }},
#                             {{
#                                 "type": "choice",
#                                 "value": "972ab1f6-0429-4263-9e52-e144e72e6287"
#                             }}
#                         ]
#                     }}
#                 }}
# '''
# str = str.format(1)
# print(str)

import re
from collections import defaultdict

label_count = defaultdict(int)
s1 = "Red Beige kW)"
s2 = "Red Beige Y1"
s3 = "Red Beige Y3"

f = re.search(r'Z\d|Y\d|X\d|kW\)', s1)
#f = re.search(r'Y\d', s2)

# print(f)
result = f.group()
print(result)
label_count[result] += 1

f = re.search(r'Z\d|Y\d|X\d|kW\)', s2)
result = f.group()
print(result)
label_count[result] += 1

f = re.search(r'Z\d|Y\d|X\d|kW\)', s3)
result = f.group()
print(result)
label_count[result] += 1


# try:
#     label_count[result] += 1
# except KeyError:
#     label_count[result] = 0
#     label_count[result] += 1

print(label_count)
for k, v in label_count.items():
    print(k, v)
