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
        
        # Define hash and unique key for CAR
        self.car_hash_key = 'retailUnit'
        self.car_unique_key = 'id'
        
        # Data is always data
        self.data_key = 'data'
        
        # Define hash and unique key for reparations
        self.reparation_hash_key = 'reparation_id'
        self.reparation_unique_key = 'id'

        # Read in data
        self.cars_data_list = format_json_data("./data/cars_data.json", self.car_hash_key, self.car_unique_key)
        self.reparations_data_list= format_json_data("./data/reparations_data.json", self.reparation_hash_key, self.reparation_unique_key)
        self.parts_data_list = []
    
        self.posted_car_ids = []
    
    # A post request to API (create)
    # If len > 0 then pop so we dont write the same line twice
    # First tasks saves cars_data_json to Redis
    @task(2)
    def create_car_post(self):   
        if len(self.cars_data_list):
            data_entry = self.cars_data_list.pop(0)
            self.client.post(
                f'/redis/hset?hash={data_entry.get(self.car_hash_key)}&key={data_entry.get(self.car_unique_key)}&value={data_entry.get(self.data_key)}',
                headers={"content-type": "application/json"},
            )
            self.posted_car_ids.append(data_entry.get(self.car_unique_key))
        else:
            exit(1)
    
    # Now we are sending reparations for those cars that are already inserted
    @task(1)
    def create_reparations_post(self):
        #data_entry = self.reparations_data_list
        if len(self.reparations_data_list) and len(self.posted_car_ids):
            car_id = self.posted_car_ids.pop(0)
            data_entry = self.reparations_data_list.pop(0)
            if data_entry.get('car_id') == car_id:
                self.client.post(
                    f'/redis/hset?hash={data_entry.get(self.reparation_hash_key)}&key={data_entry.get(self.reparation_unique_key)}&value={data_entry.get(self.data_key)}',
                    headers={"content-type": "application/json"},
                )
                self.posted_car_ids.append(data_entry.get(self.car_unique_key))
    
    wait_time = between(0,1)

# When the script is running (python locust.py), this if statement will be executed
if __name__ == "__main__":
    cars_data_list = format_json_data("./data/cars_data.json", "retailUnit", "id")
    reparations_data_list = format_json_data("./data/reparations_data.json", "car_id", "id")
    parts_data_list = format_json_data("./data/parts_data.json", "reparation_id", "id")

    #pprint.pprint(cars_data_list[0])
    #print()
    # pprint.pprint(reparations_data_list[0])
    # print()
    # pprint.pprint(parts_data_list[0])
    # print()

    