import random
from locust import HttpUser, task, between, constant, SequentialTaskSet
import redis

from data.data import format_json_data
#import data.data

print(help(data))

# Vad vill vi jämföra?
# COST - check the different costs between Redis and BT
# Integrate towards Redis and BT. Where are they going to run? GCP
# PERFORMANCE:
# 1) Query response time: The time it takes for the db to respond to a query is an important indicator of performance.
# 2) Throughput: Measures number of queries the database can handle within a period of time.

"""
class RedisUser(SequentialTaskSet):
   
    @task
    def read_from_redis(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        key = random.randint(1, 1000)
        value = r.get(key)
        print(f"Read key={key}, value={value}")

    @task
    def write_to_redis(self):
        r = redis.Redis(host='localhost', port=6379, db=0)
        key = random.randint(1, 1000)
        value = random.randint(1, 1000)
        r.set(key, value)
        print(f"Wrote key={key}, value={value}")


class MyLoadTest(HttpUser):
    host='http://localhost'
    task=[RedisUser]
""" 
