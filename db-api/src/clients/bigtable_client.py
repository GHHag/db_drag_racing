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

    # Recieves what data kind (column family) and the whole request body:
    def write_row(self, kind, request_body):
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

    def get_row(self, row_key):
        row = self.table.read_row(row_key)
        print(row_key)
        print(row.cells)
        return row.cells

    def get_family(self, family_name):
        row = self.table.row(f"{family_name}#*")
        print(self.table.name)
        filtered_cells = row.cells(self.table.name, column_family=family_name)

        return filtered_cells
