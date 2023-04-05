from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task(1)
    def create_post(self):
        self.client.get(
            "/redis/hget?hash=UA&key=52fe86a8-d222-11ed-90cb-5254004a31de",
            headers={"content-type": "application/json"},
        )


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
