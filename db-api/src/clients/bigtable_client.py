import argparse
import datetime

from google.cloud import bigtable
from google.cloud.bigtable import column_family
from google.cloud.bigtable import row_filters


# Service Layer -  business logic.


class BigtableClient:
    def __init__(self, project_id, instance_id, table_id):
        self.client = bigtable.Client(project=project_id, admin=True)
        self.instance = self.client.instance(instance_id)
        self.table = self.instance.table(table_id)

        if not self.table.exists():
            max_versions_rule = column_family.MaxVersionsGCRule(2)
            column_family_id = "cf1"
            column_families = {column_family_id: max_versions_rule}
            self.table.create(column_families=column_families)

    def write_row(self, json_data, key_prefix):
        # json_data = {
        #    'column_id1': 'somevalue',
        #    'column_id2': 'somevalue'
        # }
        row_key = f'{key_prefix}#{json_data.get("id")}'
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
        return row

    def get_family(self, family_name):
        row = self.table.row(f"{family_name}#*")
        filtered_cells = row.cells(self.table.name, column_family=family_name)
        return filtered_cells
