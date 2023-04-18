import datetime
from google.cloud import bigtable
from google.cloud.bigtable import column_family
from google.cloud.bigtable import row_filters

# Service Layer -  business logic.
# WHAT are we saving in the bigtable instance.
class BigtableClient:
    def __init__(self):
        # Setup
        # The client must be created with admin=True because it will create a table.

        self.client = bigtable.Client(project='any-project', admin=True)
        self.instance = self.client.instance('any-instance')

        print("Creating the {} table.".format(table_id))
        table = instance.table(table_id)

        print("Creating column family cf1 with Max Version GC rule...")
        # Create a column family with GC policy : most recent N versions
        # Define the GC policy to retain only the most recent 2 versions
        max_versions_rule = column_family.MaxVersionsGCRule(2)
        column_family_id = "cf1"
        column_families = {column_family_id: max_versions_rule}
        if not table.exists():
            table.create(column_families=column_families)
        else:
            print("Table {} already exists.".format(table_id))

    def insert(self):
        pass