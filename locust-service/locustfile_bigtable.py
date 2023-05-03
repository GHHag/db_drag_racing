from locust import HttpUser, task, between
from data.data import format_json_data
import pprint as pprint
import random
import json

from google.cloud import bigtable
from google.cloud.bigtable import column_family
from google.cloud.bigtable import row_filters


class MyUser(HttpUser):
    host = "http://localhost:8080"
    wait_time = between(1, 5)  # Adjust the waiting time between requests as needed

    def __init__(self, *args, **kwargs):
        super(MyUser, self).__init__(*args, **kwargs)
        self.data_key = "data"

        # Define column family and row key(?) for cars
        self.car_col_family = "cars_data"
        self.car_row_key = f"{self.car_col_family}#id"

        # Define row key and unique column family? for reparations
        self.reparation_col_family = "reparations_data"
        self.reparation_row_key = f"{self.reparation_col_family}#id"

        # Define column family and row key(?) for parts
        self.part_col_family = "parts_data"
        self.part_row_key = f"{self.part_col_family}#id"

        self.car_data_list = format_json_data("./data/cars_data.json", "id", "id")
        self.reparations_data_list = format_json_data(
            "./data/reparations_data.json", "id", "id"
        )
        self.parts_data_list = format_json_data("./data/parts_data.json", "id", "id")

    @task
    def create_car_post(self):
        if len(self.car_data_list):
            data_entry = self.car_data_list.pop(0)
            self.client.post(
                f"/bigtable/write?kind={self.car_col_family}", json=data_entry
            )


"""
#OLD JSON DATA
# Test JSON data
data_to_send = [
    {"id": "1", "column_id1": "value1", "column_id2": "value2"},
    {"id": "2", "column_id1": "value3", "column_id2": "value4"},
    # Add more JSON objects as needed
]
"""

# DATA STRUCTURE FOR write_row_gpt()
# JSON object to save as a row
# json_data = {"id": "1", "column_id1": "value1", "column_id2": "value2"}

"""
class BigtableWriteUser(HttpUser):
    host = "http://localhost:8080"  # Set the base host here
    wait_time = between(1, 5)  # Adjust the waiting time between requests as needed

    @task
    def write_to_bigtable(self):
        for data in json_data:
            headers = {"Content-Type": "application/json"}
            self.client.post("/bigtable/write", data=json.dumps(data), headers=headers)
"""
