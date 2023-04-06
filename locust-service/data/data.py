import requests
import json
import pprint as pprint

# Läser in och formaterar datan som skickas sedan till Redis server
# Detta kan bli en Locust fil!


def format_json_data(json_file_path, hash_key, unique_key):
    formatted_data_list = []
    with open(json_file_path, "r") as file:
        json_data = json.loads(file.read())
        for data_dict in json_data:
            
            hash_ = data_dict.get(hash_key)
            key = data_dict.get(unique_key)
            data = {
                k: v for k, v in data_dict.items() if k not in [hash_key, unique_key]
            }
            data_str = json.dumps(data)
            formatted_data_list.append(
                {hash_key: hash_, unique_key: key, "data": data_str}
            )
            # requests.post(
            #    f"http://localhost:8080/redis/hset?hash={retail_unit}&key={id}&value={data_str}"
            # )

    return formatted_data_list


if __name__ == "__main__":
    cars_data_list = format_json_data("cars_data.json", "retailUnit", "id")
    reparations_data_list = format_json_data("reparations_data.json", "car_id", "id")
    parts_data_list = format_json_data("parts_data.json", "reparation_id", "id")

    pprint.pprint(cars_data_list[0])
    print()
    pprint.pprint(reparations_data_list[0])
    print()
    pprint.pprint(parts_data_list[0])
    print()
