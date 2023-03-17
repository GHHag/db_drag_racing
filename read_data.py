import json

with open('generated_data.json', 'r') as file:
    #json_data = json.loads(file.read())
    json_data = file.read()
    #print(json_data)
    #print(type(json_data))
    #print(len(json_data))
    x = json_data.split('{')
    for i in x:
        print(i)
        input()