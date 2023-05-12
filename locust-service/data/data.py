import requests
import json
import pprint as pprint

# Läser in och formaterar datan som skickas sedan till Redis and Bigtable server


"""
Formats and returns data from a json file.
    @param json_file_path - File path to a .json file
    @param hash_key - The key of the json data to be used as hash key
    @param unique_key - The key of the json data to be used as unique key
"""


def format_json_data(json_file_path, hash_key, unique_key):
    formatted_data_list = []
    with open(json_file_path, "r") as file:
        json_data = json.loads(file.read())
        for data_dict in json_data:
            # Selection for provided values of hash_key and unique_key
            if hash_key or unique_key is not None:
                hash_ = data_dict.get(hash_key)
                key = data_dict.get(unique_key)
                data = {
                    k: v
                    for k, v in data_dict.items()
                    if k not in [hash_key, unique_key]
                }
                data_str = json.dumps(data)
                formatted_data_list.append(
                    {hash_key: hash_, unique_key: key, "data": data_str}
                )
            else:
                formatted_data_list.append(data_dict)

    return formatted_data_list


if __name__ == "__main__":
    # Call the format_json_data function and pass argument for the hashes and keys to be used
    # for querying the data
    # cars_data_list = format_json_data("cars_data.json", "id", "id")
    # reparations_data_list = format_json_data("reparations_data.json", "id", "id")
    # parts_data_list = format_json_data("parts_data.json", "id", "id")

    cars_data_list = format_json_data("cars_data.json", None, None)

    pprint.pprint(cars_data_list[0])
    print()
    # pprint.pprint(reparations_data_list[0])
    # print()
    # pprint.pprint(parts_data_list[0])
    # print()
    # print(len(cars_data_list))
