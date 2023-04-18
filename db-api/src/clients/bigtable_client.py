from google.cloud import bigtable

# Service Layer -  business logic.
# WHAT are we saving in the bigtable instance.
class BigtableClient:
    def __init__(self):
        # Setup
        # The client must be created with admin=True because it will create a table.

        self.client = bigtable.Client(project='any-project', admin=True)
        self.instance = self.client.instance('any-instance')

    def insert(self):
        pass