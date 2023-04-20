import argparse
import datetime

from google.cloud import bigtable
#from google.cloud.bigtable import column_family
#from google.cloud.bigtable import row_filters


# Service Layer -  business logic.
# WHAT are we saving in the redis instance.


class BigtableClient:
    def __init__(self, project_id, instance_id, table_id):
        client = bigtable.Client(project=project_id, admin=True)
        instance = client.instance(instance_id)

        self.project_id = project_id
        self.instance_id = instance_id
        self.table_id = table_id

        # Create Bigtable client and table objects
        self.client = bigtable.Client()
        self.instance = self.client.instance(self.instance_id)
        self.table = self.instance.table(self.table_id)

        # Create column family if it doesn't exist
        self._create_column_family("cf1")

    def _create_column_family(self, column_family_id):
        column_families = {column_family_id: None}
        self.table.create(column_families=column_families)

    def write_row(self, json_data, key_prefix):
        #json_data = {
        #    'column_id1': 'somevalue',
        #    'column_id2': 'somevalue'
        #}
        row_key = f'{key_prefix}#{json_data.get("id")}'
        row = self.table.row(row_key)
        for key, value in json_data.items():
            # family name = cars / reparations / parts
            row.set_cell('insert_family_name_here', key, value)

        row.commit()
        return (200, {"message": "OK"})

    def get_row(self, row_key):
        row = self.table.row(row_key)
        return row

    def get_family(self, family_name):
        row = self.table.row(f'{family_name}#*')
        return row


"""
{
  "retailUnit": "CN",
  "id": "1b2619d2-dabd-11ed-b2f7-2cfda1b6d771",
  "reparation_ids": [
    "1b261a40-dabd-11ed-b2f7-2cfda1b6d771",
    "1b261e50-dabd-11ed-b2f7-2cfda1b6d771",
    "1b262440-dabd-11ed-b2f7-2cfda1b6d771",
    "1b262a30-dabd-11ed-b2f7-2cfda1b6d771",
    "1b262c60-dabd-11ed-b2f7-2cfda1b6d771",
    "1b262f30-dabd-11ed-b2f7-2cfda1b6d771",
    "1b26323c-dabd-11ed-b2f7-2cfda1b6d771",
    "1b263778-dabd-11ed-b2f7-2cfda1b6d771",
    "1b26387c-dabd-11ed-b2f7-2cfda1b6d771",
    "1b263b1a-dabd-11ed-b2f7-2cfda1b6d771",
    "1b263e8a-dabd-11ed-b2f7-2cfda1b6d771",
    "1b2640f6-dabd-11ed-b2f7-2cfda1b6d771",
    "1b2645e2-dabd-11ed-b2f7-2cfda1b6d771",
    "1b264966-dabd-11ed-b2f7-2cfda1b6d771",
    "1b264dbc-dabd-11ed-b2f7-2cfda1b6d771",
    "1b264f24-dabd-11ed-b2f7-2cfda1b6d771",
    "1b26528a-dabd-11ed-b2f7-2cfda1b6d771"
  ],
  "date": "11/20/2022",
  "carvin": "WBSBL93456P534106",
  "paint": "Mauv",
  "manufacturer": "Scion",
  "model": "Sorento"
}
"""