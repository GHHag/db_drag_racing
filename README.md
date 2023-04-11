# db_drag_racing

# A general README.md - DatabaseDragRacing

The layout is the following:
We have two folders (db-api/ and locust-service/), ie two microservices.

Inside each folder there is a README.md file.
Follow the instructions in both the README.md to get started.

### Basic setup of the application

1. db-api -> is where the api is.

2. locust-service -> data/ and locust files

---

### Data/ part:

- MOCK_DATA.json -> is generated mockdata from mockaroo
- generate_data.py -> when ran, it created three files with mock data: cars_data.json, parts_data.json and reparations_data.py
- data.py -> reads the created files from generate_data.py and formats it, so it can be sent into Redis.

---

### Locust part:

- locustfile.py -> main test file.
