# db_drag_racing

# A general README.md - DatabaseDragRacing

- Requirements: Python 3

### The layout is the following:

We have two folders (db-api/ and locust-service/), ie two microservices.

Inside each folder there is a README.md file.
Follow the instructions in both the README.md to get started.

### Basic setup of the application:

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

---

### To launch api and run tests:

1. Activate virtual env in both db-api/ and locust-service/ (read the readme in how to do that inside those folders).

2. Open the API connection by cd into db-api/ and run in one terminal:

```
python app.py
```

3. Start the locust file in order to run the tests, cd into locust-service/ and run in another terminal:

```
locust -f locustfile.py
```
