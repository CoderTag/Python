import json
import re
import sys
import csv
from collections import defaultdict

while(True):
    try:
        user_input = int(input("Choose an option 1 or 2 (1. Create csv template and 2. create updated json): "))
        if (user_input > 0) and (user_input < 3):
            break
    except ValueError:
        pass

if user_input == 1:
    while True:
        json_file = input("Provide json file: ")
        if re.search(r'.*\.json\b', json_file):
            break

    while True:
        csv_file = input("Provide output csv file: ")
        if re.search(r'.*\.csv\b', csv_file):
            break

if user_input == 2:
    while True:
        csv_file = input("Provide input csv file: ")
        if re.search(r'.*\.csv\b', csv_file):
            break

    while True:
        json_file_input = input("Provide input json file: ")
        if re.search(r'.*\.json\b', json_file_input):
            break

    while True:
        json_file_output = input("Provide output json file: ")
        if re.search(r'.*\.json\b', json_file_output):
            break


if user_input == 1:
    # with open('t.json') as f:
    with open(json_file) as f:
        data = json.load(f)

    my_keys = ['id', 'attachment', 'description', 'randomize']
    my_fields = []
    ref_count = []
    for f in data['fields']:
        prop = {}
        if 'properties' not in f.keys():
            continue
        if 'choices' not in f['properties'].keys():
            continue
        choices = []
        choices = f['properties']['choices']
        flag = True

        for choice in choices:
            if re.search(r'Z\d|Y\d|X\d|kW\)', choice['label']):
                flag = False
                # (my_year, my_title) = re.findall(r'^\d+\s+(?:GREAT|BAD)', f['title'])[0].split(" ")
                my_fields.append({
                    "title": f["title"],
                    "q_ref": f["ref"],
                    "label": choice["label"],
                    "c_ref": choice["ref"]
                })
                # Find number of choice reference in the document
                ref_count.append(choice["ref"])

        if flag == "True":
            continue
    # print(ref_count)

    label_count = defaultdict(int)

    # with open('typeform.csv', 'w') as csvfile:
    with open(csv_file, 'w') as csvfile:
        #writer = csv.DictWriter(csvfile, fieldnames=["title", "q_ref", "label", "c_ref", "count", "score", "price"])
        writer = csv.DictWriter(csvfile, fieldnames=["title", "q_ref", "label", "c_ref", "score", "price"])
        writer.writeheader()
        for field in my_fields:
            # count = ref_count.count(field['c_ref'])
            # field['count'] = count
            field['score'] = 5
            field['price'] = 30
            writer.writerow(field)

            found = re.search(r'Z\d|Y\d|X\d|kW\)', field['label'])
            if found:
                found = found.group()
            label_count[found] += 1

            # for k, v in field.items():
            #     print(f'{k}: {v}', end=", ")
            # print("\n")

for k, v in label_count.items():
    print(f'{k} = {v}')

if user_input == 2:
    # with open('t.json') as f:
    with open(json_file_input) as f:
        data = json.load(f)

    add_json = '''
    {{
        "action": "add",
        "details": {{
            "target": {{
                "type": "variable",
                "value": {0}
            }},
            "value": {{
                "type": "constant",
                "value": {1}
            }}
        }},
        "condition": {{
            "op": "is",
            "vars": [
                {{
                    "type": "field",
                    "value": {2}
                }},
                {{
                    "type": "choice",
                    "value": {3}
                }}
            ]
        }}
    }}
    '''

    # with open('typeform.csv', 'r') as csvfile:
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for ln in reader:
            for f in data['logic']:
                if ln['q_ref'] != f['ref']:
                    continue
                actions = f['actions']

                score_not_found = True
                price_not_found = True

                for action in actions:
                    if action['action'] == 'jump':
                        continue

                    if action['details']['target']['value'] == 'score':
                        vars = action['condition']['vars']
                        for v in vars:
                            if v['value'] == ln['c_ref']:
                                action['details']['value']['value'] = ln['score']
                                score_not_found = False

                    if action['details']['target']['value'] == 'price':
                        vars = action['condition']['vars']
                        for v in vars:
                            if v['value'] == ln['c_ref']:
                                action['details']['value']['value'] = ln['price']
                                price_not_found = False

                if score_not_found:
                    add_json = add_json.format('score', ln['score'], ln['q_ref'], ln['c_ref'])
                    actions.append(add_json)

                if price_not_found:
                    add_json = add_json.format('price', ln['price'], ln['q_ref'], ln['c_ref'])
                    actions.append(add_json)

    # with open('t2.json', 'w') as f:
    with open(json_file_output, 'w`') as f:
        json.dump(data, f, indent=2)
