from google.cloud import bigtable

# The client must be created with admin=True because it will create a
# table.
client = bigtable.Client(project='any-project', admin=True)
instance = client.instance('any-instance')

