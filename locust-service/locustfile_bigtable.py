from locust import HttpUser, task, between
from data.data import format_json_data
import pprint as pprint
import random


# MyUser ärver från HTTPUser
class MyUser(HttpUser):
    host = "http://localhost:8080"
