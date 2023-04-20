from google.cloud import bigtable


class BigtableClient:
    def __init__(self, project_id, instance_id, table_id):
        self.project_id = project_id
        self.instance_id = instance_id
        self.table_id = table_id

        # Set environment variables
        self._set_env_vars()

        # Create Bigtable client and table objects
        self.client = bigtable.Client()
        self.instance = self.client.instance(self.instance_id)
        self.table = self.instance.table(self.table_id)

        # Create column family if it doesn't exist
        self._create_column_family("cf1")

    def _set_env_vars(self):
        import os

        os.environ["BIGTABLE_EMULATOR_HOST"] = "localhost:8086"
        os.environ["BIGTABLE_PROJECT_ID"] = self.project_id
        os.environ["BIGTABLE_INSTANCE_ID"] = self.instance_id

    def _create_column_family(self, column_family_id):
        column_families = {column_family_id: None}
        self.table.create(column_families=column_families)

    def write_row(self, row_key, column_family_id, column_id, value):
        row = self.table.row(row_key)
        row.set_cell(column_family_id, column_id, value)
        row.commit()
