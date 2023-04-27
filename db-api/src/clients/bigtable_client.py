import argparse
import datetime
import json

from google.cloud import bigtable
from google.cloud.bigtable import column_family
from google.cloud.bigtable import row_filters


# Service Layer -  business logic.


class BigtableClient:
    def __init__(self, project_id, instance_id, table_id):
        self.client = bigtable.Client(project=project_id, admin=True)
        self.instance = self.client.instance(instance_id)
        self.table = self.instance.table(table_id)
        max_versions_rule = column_family.MaxVersionsGCRule(2)
        self.column_families = {
            "cars_data": max_versions_rule,
            "reparations_data": max_versions_rule,
            "parts_data": max_versions_rule,
        }

        if not self.table.exists():
            self.table.create(column_families=self.column_families)

    """
    DATA STRUCTURE FOR write_row_gpt()
    # JSON object to save as a row
    json_data = {
        "id": "1",
        "column_id1": "value1",
        "column_id2": "value2"
    }
    """

    # Recieves what data kind (column family) and the whole request body:
    def write_row_gpt(self, kind, request_body):
        if kind not in self.column_families.keys():
            raise Exception("Invalid column family")
        # Write the JSON object as a row in Bigtable
        row_key = f"{kind}#{request_body.get('id')}"
        # Loops and Writes each cell for the row (JSON object)
        row = self.table.row(row_key)
        for key, value in request_body.items():
            row.set_cell(
                str(kind), str(key).encode("utf-8"), str(value).encode("utf-8")
            )
        row.commit()
        print(f"Row with key '{row_key}' written to Bigtable.")
        return {"message": "OK"}

    def write_row(self, json_data):
        # json_data = {
        #    'column_id1': 'somevalue',
        #    'column_id2': 'somevalue'
        # }
        row_key = f'{json_data.get("id")}'
        print(row_key)
        row = self.table.row(row_key)
        for key, value in json_data.items():
            # family name = cars / reparations / parts
            row.set_cell("cf1", key, value)

        row.commit()
        # return (200, {"message": "OK"})
        return {"message": "OK"}

    def get_row(self, row_key):
        row = self.table.read_row(row_key)
        # convert all values to str to handle bytearray
        # For all values in row, execute str(value, "UTF-8")

        return json.dumps({k: str(v) for k, v in row.items()})
        return row

    def get_family(self, family_name):
        row = self.table.row(f"{family_name}#*")
        filtered_cells = row.cells(self.table.name, column_family=family_name)
        return filtered_cells
