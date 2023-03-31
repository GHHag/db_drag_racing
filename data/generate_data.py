import random
import uuid
import json

with open('MOCK_DATA.json', 'r') as file:
    json_data = json.loads(file.read())

    data_dict = {}
    for object in json_data:
        for k, v in object.items():
            if k in data_dict:
                data_dict[k].append(v)
            else:
                data_dict[k] = [v]

    data = []
    for i in range(100000):
        row = {}
        for k, v in data_dict.items():
            if k == 'id':
                row[k] = str(uuid.uuid1())
                continue
            length = len(data_dict[k])
            random_num = random.randint(0, length)
            row[k] = data_dict[k][random_num - 1]
        data.append(row)

    json_string = json.dumps([x for x in data])
    with open('generated_data.json', 'w') as write_file:
        #json.dump(json_string, write_file)
        write_file.write(json_string)