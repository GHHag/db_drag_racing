from locust import HttpUser, task
from data.data import format_json_data
import pprint as pprint

# class MyUser(HttpUser):
#     # host: "/db-api/src/app.py"

#     @task
#     def create_post(self):
#         self.client.post(
#             "/redis/hset?hash=PT&key=a0014cde-ea93-4d95-8260-273198c50a95",
#             headers={"content-type": "application/json"},
#         )

# When the script is running (python locust.py), this if statement will be executed
if __name__ == "__main__":
    cars_data_list = format_json_data("./data/cars_data.json", "retailUnit", "id")
    reparations_data_list = format_json_data("./data/reparations_data.json", "car_id", "id")
    parts_data_list = format_json_data("./data/parts_data.json", "reparation_id", "id")

    pprint.pprint(cars_data_list[0])
    print()
    pprint.pprint(reparations_data_list[0])
    print()
    pprint.pprint(parts_data_list[0])
    print()

