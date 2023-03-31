import json

with open('generated_data.json', 'r') as file:
    json_data = json.loads(file.read())
    for i in json_data:
        print(i)
        input()
