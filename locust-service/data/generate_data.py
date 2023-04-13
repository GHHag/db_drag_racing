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


# Open file containing mock data
with open("MOCK_DATA.json", "r") as file:
    # json_data är själva MOCK_DATA
    json_data = json.loads(file.read())

    data_dict = {}
    for object in json_data:
        # Collect all unique values and append to a list for each key
        for k, v in object.items():
            if k in data_dict:
                data_dict[k].append(v)
            else:
                data_dict[k] = [v]
    """
    How the above function is creating/reworking the data
    output_from_above_logic = {
        "retailUnit": ["PT", "DK", "...", "..."],
        "id": [
            "a0014cde-ea93-4d95-8260-273198c50a95",
            "a0014cde-ea93-4d95-8260-273198c51337",
            "...",
            "...",
        ],
        "date": ["similar list thingy"],
        "...": "...",
    }
    """
    data = []
    reperations_operators = ['Operator1', 'Operator2', 'Operator3', 'Operator4', 'Operator5', 'Operator6', 'Operator7', 'Operator8','Operator9', 'Operator10', 'Operator11', 'Operator12', 'Operator13', 'Operator14', 'Operator15', 'Operator16', 'Operator17', 'Operator18', 'Operator19', 'Operator20']
    # Iterate a given number of times to generate that amount of data entries
    # for i in range(100000):
    for i in range(100):
        row = {}
        # Every car will have relations with data for reparations and reparations
        # will in turn have relations with parts
        reparations = []
        parts = []
        for k, v in data_dict.items():
            if k == "id":
                row[k] = str(uuid.uuid1())

                # Create instances of reparations and parts
                row["reparation_ids"] = []
                for i in range(random.randint(1, 20)):
                    reparation_id = str(uuid.uuid1())

                    # Create instances of the Part class
                    part_ids = []
                    for n in range(random.randint(1, 15)):
                        part_id = str(uuid.uuid1())
                        parts.append(Part(part_id, reparation_id, "Some part name"))
                        part_ids.append(part_id)

                    # Create instance of the Reparations class
                    reparations.append(
                        Reparation(
                            reparation_id,
                            row[k],
                            str(dt.datetime.now()),
                            random.randint(1500, 30000),
                            "Reparation note",
                            reperations_operators[random.randint(0,len(reperations_operators)-1)],     
                            part_ids,
                        )
                    )
                    row["reparation_ids"].append(reparation_id)
                continue
            # Generate random value for the carvin key
            if k == "carvin":
                row[k] = str(uuid.uuid1())

            length = len(data_dict[k])
            random_num = random.randint(0, length)
            row[k] = data_dict[k][random_num - 1]
        data.append(row)

    cars_json_data = json.dumps([x for x in data])
    reparations_json_data = json.dumps([dataclasses.asdict(x) for x in reparations])
    parts_json_data = json.dumps([dataclasses.asdict(x) for x in parts])

    with open("cars_data.json", "w") as write_file:
        write_file.write(cars_json_data)

    with open("reparations_data.json", "w") as write_file:
        write_file.write(reparations_json_data)

    with open("parts_data.json", "w") as write_file:
        write_file.write(parts_json_data)
