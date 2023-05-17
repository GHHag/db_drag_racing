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
    # wait_time = between(1, 2)  # Adjust the waiting time between requests as needed

    def __init__(self, *args, **kwargs):
        super(MyUser, self).__init__(*args, **kwargs)
        self.data_key = "data"

        # Define column family and row key(?) for cars
        self.car_col_family = "cars_data"
        self.car_row_key = "id"

        # Define row key and unique column family? for reparations
        self.reparation_col_family = "reparations_data"
        self.reparation_row_key = "id"

        # Define column family and row key(?) for parts
        self.part_col_family = "parts_data"
        self.part_row_key = "id"

        self.cars_data_list = format_json_data("./data/cars_data.json", None, None)
        print(len(self.cars_data_list))
        self.reparations_data_list = format_json_data(
            "./data/reparations_data.json", None, None
        )
        self.parts_data_list = format_json_data("./data/parts_data.json", None, None)
        # When we want to READ (cRud) the created objects, we want to retrieve unique hashes and ids
        # self.car_hashes = set()
        self.car_ids = []
        # self.reparation_hashes = set()
        self.reparation_ids = []
        # self.part_hashes = set()
        self.part_ids = []

    # WRITE
    @task
    def create_car_post(self):
        if len(self.cars_data_list):
            data_entry = self.cars_data_list.pop(0)
            self.client.post(
                f"/bigtable/write?kind={self.car_col_family}", json=data_entry
            )
            self.car_ids.append(data_entry.get(self.car_row_key))
        else:
            pass

    @task
    def create_reparations_post(self):
        if len(self.reparations_data_list):
            data_entry = self.reparations_data_list.pop(0)
            self.client.post(
                f"/bigtable/write?kind={self.reparation_col_family}", json=data_entry
            )
            self.reparation_ids.append(data_entry.get(self.reparation_row_key))
        else:
            pass

    @task
    def create_part_post(self):
        if len(self.parts_data_list):
            data_entry = self.parts_data_list.pop(0)
            self.client.post(
                f"/bigtable/write?kind={self.part_col_family}", json=data_entry
            )
            self.part_ids.append(data_entry.get(self.part_row_key))
        else:
            pass

    # READ CARS
    @task
    def get_car(self):
        if len(self.car_ids) >= 1:
            random_id_index = random.randint(0, len(self.car_ids) - 1)
            car_id = self.car_ids[random_id_index]
            response = self.client.get(
                f"/bigtable/read?row_key={self.car_col_family}&row_id={car_id}"
            )
            if response.status_code == 200:
                # too much to unpack
                print(*response)
            else:
                pass

    # READ Reparations
    @task
    def get_reparation(self):
        if len(self.reparation_ids) >= 1:
            random_id_index = random.randint(0, len(self.reparation_ids) - 1)
            reparation_id = self.reparation_ids[random_id_index]
            response = self.client.get(
                f"/bigtable/read?row_key={self.reparation_col_family}&row_id={reparation_id}"
            )
            if response.status_code == 200:
                # unpack and print response value
                print(*response)
            else:
                pass

    # READ Parts
    @task
    def get_part(self):
        if len(self.part_ids) >= 1:
            random_id_index = random.randint(0, len(self.part_ids) - 1)
            part_id = self.part_ids[random_id_index]
            response = self.client.get(
                f"/bigtable/read?row_key={self.part_col_family}&row_id={part_id}"
            )
            if response.status_code == 200:
                # unpack response tuple and print response value
                print(*response)
            else:
                pass

    # DELETE Cars
    @task
    def delete_car(self):
        if len(self.car_ids) >= 1:
            random_id_index = random.randint(0, len(self.car_ids) - 1)
            car_id = self.car_ids.pop(random_id_index)
            response = self.client.delete(
                f"/bigtable/delete?row_key={self.car_col_family}&row_id={car_id}"
            )
            if response.status_code == 200:
                print(f"DELETED SUCCESSFULLY {car_id} id")
            else:
                pass

    # DELETE Reparation
    @task
    def delete_reparation(self):
        if len(self.reparation_ids) >= 1:
            random_id_index = random.randint(0, len(self.reparation_ids) - 1)
            reparation_id = self.reparation_ids.pop(random_id_index)
            response = self.client.delete(
                f"/bigtable/delete?row_key={self.reparation_col_family}&row_id={reparation_id}"
            )
            if response.status_code == 200:
                print(f"DELETED SUCCESSFULLY {reparation_id} id")
            else:
                pass

    # DELETE Part
    @task
    def delete_part(self):
        if len(self.part_ids) >= 1:
            random_id_index = random.randint(0, len(self.part_ids) - 1)
            part_id = self.part_ids.pop(random_id_index)
            response = self.client.delete(
                f"/bigtable/delete?row_key={self.part_col_family}&row_id={part_id}"
            )
            if response.status_code == 200:
                print(f"DELETED SUCCESSFULLY {part_id} id")
            else:
                pass
