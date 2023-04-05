from locust import HttpUser, task


class MyUser(HttpUser):
    @task(1)
    def create_post(self):
        self.client.post(
            "/redis/hset?hash=UA&key=52fe86a8-d222-11ed-90cb-5254004a31de",
            headers={"content-type": "application/json"},
        )


class WebsiteUser(HttpUser):
    task_set = MyUser
