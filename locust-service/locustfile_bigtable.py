from locust import HttpUser, task, between
from google.cloud import bigtable
from data.data import format_json_data
import pprint as pprint
import random
import json

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
json_data = {"id": "1", "column_id1": "value1", "column_id2": "value2"}


class BigtableWriteUser(HttpUser):
    host = "http://localhost:8080"  # Set the base host here
    wait_time = between(1, 5)  # Adjust the waiting time between requests as needed

    @task
    def write_to_bigtable(self):
        for data in json_data:
            headers = {"Content-Type": "application/json"}
            self.client.post("/bigtable/write", data=json.dumps(data), headers=headers)
