from locust import HttpUser, task, between
from data.data import format_json_data
import pprint as pprint
import random


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
        self.part_hash_key = "name"
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
        # When we want to READ (cRud) the created objects, we want to retrieve unique hashes and ids
        self.car_hashes = set()
        self.car_ids = {} # { PT: [car_id1, car_id2], RU: [] }
        self.reparation_hashes = set()
        self.reparation_ids = []
        self.part_hashes = set()
        self.part_ids = []
        
    # A post request to API (create)
    # If len > 0 then pop so we dont write the same line twice
    # First tasks saves cars_data_json to Redis

    # WRITE (Crud)
    @task
    def create_car_post(self):
        if len(self.cars_data_list):
            data_entry = self.cars_data_list.pop(0)
            self.client.post(
                f"/redis/hset?hash={data_entry.get(self.car_hash_key)}&key={data_entry.get(self.car_unique_key)}&value={data_entry.get(self.data_key)}",
                headers={"content-type": "application/json"},
            )
            # pushes the car hash key to a set
            self.car_hashes.add(data_entry.get(self.car_hash_key))
            #self.car_ids.append(data_entry.get(self.car_unique_key))
            # if the list of car ids for the retailunit exists, append to it, else create a new list
            if data_entry.get(self.car_hash_key) in self.car_ids:
                self.car_ids[data_entry.get(self.car_hash_key)].append(data_entry.get(self.car_unique_key))
            else:
                self.car_ids[data_entry.get(self.car_hash_key)] = [data_entry.get(self.car_unique_key)]
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
            self.reparation_hashes.add(data_entry.get(self.reparation_hash_key))
            self.reparation_ids.append(data_entry.get(self.reparation_unique_key))
      
    @task
    def create_parts_post(self):
        if len(self.parts_data_list):
            data_entry = self.parts_data_list.pop(0)
            self.client.post(
                f"/redis/hset?hash={data_entry.get(self.part_hash_key)}&key={data_entry.get(self.part_unique_key)}&value={data_entry.get(self.data_key)}",
                headers={"content-type": "application/json"},
            )
            self.part_hashes.add(data_entry.get(self.part_hash_key))
            self.part_ids.append(data_entry.get(self.part_unique_key))

    wait_time = between(0, 1)
    
    # READ
    @task
    def get_car_hash(self):
        # how do we get an item from a random index of the set? 
        random_car_hash = self.car_hashes[random.randint(0, len(self.car_hashes) - 1)]
        random_car_id = self.car_ids.get(random_car_hash)[random.randint(0, len(self.car_ids.get(random_car_hash)) - 1)]

        response = self.client(f'/redis/hget?hash={random_car_hash}&key={random_car_id}')
        if response.status.status_code == 200:
            redis_hash = response.json()
            print(redis_hash)
        else:
            pass

"""
# READ (cRud), New Class?
@task
def get_redis_hash(self):
redis_hash_key = "my_hash_key"
response = self.client.get(f"/my/api/endpoint?redis_hash_key={redis_hash_key}")

if response.status_code == 200:
    redis_hash = response.json()
    # Do something with the Redis hash
    
else:
    print(f"Error retrieving Redis hash: {response.status_code}")
"""

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
