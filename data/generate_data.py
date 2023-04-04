import random
import uuid
import json
import dataclasses
from dataclasses import dataclass
import datetime as dt

"""
TODO: 
-Accept command line argument for the number of rows to generate
-Replace hard coded values if needed
"""


@dataclass
class Reparation:
    id: str
    car_id: str
    date: dt.datetime
    cost: float
    note: str
    operator: str
    part_ids: list


@dataclass
class Part:
    id: str
    reparation_id: str
    name: str


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
    #for i in range(100000):
    for i in range(10):
        row = {}
        reparations = []
        parts = []
        for k, v in data_dict.items():
            if k == 'id':
                row[k] = str(uuid.uuid1())
                #row['reparations'] = []
                row['reparation_ids'] = []
                for i in range(random.randint(1, 20)):
                    reparation_id = str(uuid.uuid1())
                    part_ids = []
                    for n in range(random.randint(1, 15)):
                        part_id = str(uuid.uuid1())
                        parts.append(Part(
                            part_id, reparation_id, 
                            "Some part name"
                        ))
                        part_ids.append(part_id)
                    #row['reparations'].append(Reparation(
                    reparations.append(Reparation(
                        reparation_id, row[k], str(dt.datetime.now()),
                        random.randint(1500, 30000), "Reparation note",
                        "Byggare Bob", part_ids
                    ))
                    row['reparation_ids'].append(reparation_id)
                continue
            length = len(data_dict[k])
            random_num = random.randint(0, length)
            row[k] = data_dict[k][random_num - 1]
        data.append(row)

    cars_json_data = json.dumps([x for x in data])
    reparations_json_data = json.dumps([dataclasses.asdict(x) for x in reparations])
    parts_json_data = json.dumps([dataclasses.asdict(x) for x in parts])

    with open('cars_data.json', 'w') as write_file:
        write_file.write(cars_json_data)

    with open('reparations_data.json', 'w') as write_file:
        write_file.write(reparations_json_data)

    with open('parts_data.json', 'w') as write_file:
        write_file.write(parts_json_data)
