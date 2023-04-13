from locust import HttpUser, task, between
from data.data import format_json_data
import pprint as pprint


# MyUser ärver från HTTPUser
class MyUser(HttpUser):
    host = "http://localhost:8080"

    # Constructor
    def __init__(self, *args, **kwargs):
        # Call constructor of super class (HTTPUser)
        super(MyUser, self).__init__(*args, **kwargs)

        self.data_key = "data"

        # Define hash and unique key for cars
        self.car_hash_key = "retailUnit"
        self.car_unique_key = "id"

        # Define hash and unique key for reparations
        # self.reparation_hash_key = 'reparation_id'
        self.reparation_hash_key = "operator"
        self.reparation_unique_key = "id"

        # Define hash and unique key for parts
        self.part_hash_key = "id"
        self.part_unique_key = "id"

        # Read in data
        self.cars_data_list = format_json_data(
            "./data/cars_data.json", self.car_hash_key, self.car_unique_key
        )
        self.reparations_data_list = format_json_data(
            "./data/reparations_data.json",
            self.reparation_hash_key,
            self.reparation_unique_key,
        )
        self.parts_data_list = format_json_data(
            "./data/parts_data.json", self.part_hash_key, self.part_unique_key
        )

    # A post request to API (create)
    # If len > 0 then pop so we dont write the same line twice
    # First tasks saves cars_data_json to Redis

    @task
    def create_car_post(self):
        if len(self.cars_data_list):
            data_entry = self.cars_data_list.pop(0)
            self.client.post(
                f"/redis/hset?hash={data_entry.get(self.car_hash_key)}&key={data_entry.get(self.car_unique_key)}&value={data_entry.get(self.data_key)}",
                headers={"content-type": "application/json"},
            )
        else:
            pass
            # exit(1)

    @task
    def create_reparations_post(self):
        if len(self.reparations_data_list):
            data_entry = self.reparations_data_list.pop(0)
            self.client.post(
                f"/redis/hset?hash={data_entry.get(self.reparation_hash_key)}&key={data_entry.get(self.reparation_unique_key)}&value={data_entry.get(self.data_key)}",
                headers={"content-type": "application/json"},
            )

    @task
    def create_parts_post(self):
        if len(self.parts_data_list):
            data_entry = self.parts_data_list.pop(0)
            self.client.post(
                f"/redis/hset?hash={data_entry.get(self.part_hash_key)}&key={data_entry.get(self.part_unique_key)}&value={data_entry.get(self.data_key)}",
                headers={"content-type": "application/json"},
            )

    wait_time = between(0, 1)


# When running this script (python locust.py), this if statement will be executed
if __name__ == "__main__":
    cars_data_list = format_json_data("./data/cars_data.json", "retailUnit", "id")
    reparations_data_list = format_json_data(
        "./data/reparations_data.json", "car_id", "id"
    )
    parts_data_list = format_json_data("./data/parts_data.json", "reparation_id", "id")

    # pprint.pprint(cars_data_list[0])
    # print()
    # pprint.pprint(reparations_data_list[0])
    # print()
    # pprint.pprint(parts_data_list[0])
    # print()
