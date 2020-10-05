import json

people_string = '''
{
    "people": [
        {
            "name": "Nakul Pakul",
            "phone": "23242",
            "email": "nakul@pakul.com",
            "has_license": false
        },
        {
            "name": "Pistu Bistu",
            "phone": "7898",
            "email": "pistu@bistu.com",
            "has_license": true
        }
    ]
}
'''

# print(people_string)
data = json.loads(people_string)
print(data)
print(type(data))
print(data.keys())
print(data['people'])
for person in data['people']:
    print(person)
    print(type(person))
    del person['phone']
print(data['people'])

# now dump the new json file
new_string = json.dumps(data)
print(new_string)
new_string = json.dumps(data, indent=2)
print(new_string)
