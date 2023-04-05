from locust import HttpUser, task


class MyUser(HttpUser):
    # host: "/db-api/src/app.py"

    @task
    def create_post(self):
        self.client.post(
            "/redis/hset?hash=PT&key=a0014cde-ea93-4d95-8260-273198c50a95",
            headers={"content-type": "application/json"},
        )
