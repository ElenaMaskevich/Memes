import requests
import random


from locust import task, HttpUser


class MemeUser(HttpUser):
    token: str
    
    def on_start(self):
        response = self.client.post('/authorize', json={"name": "maskevich"}).json()
        self.token = response['token']

    @task(1)
    def get_all_memes(self):
        self.response = self.client.get('/meme', headers={
            'Authorization': self.token})

    @task(3)
    def create_meme(self):
        payload = {
            "info": {"elena": "testing"},
            "tags": [
                "memes",
                "another tag"
            ],
            "text": "Some meme",
            "url": "www.testsetset.com"
        }
        self.response = self.client.post(
            '/meme',
            json=payload,
            headers={
            'Authorization': self.token}
        )

    @task(4)
    def get_meme(self):
        headers = {"Authorization": self.token}
        meme_id = random.randrange(1, 101)
        self.client.get(f'/meme/{meme_id}', headers=headers)
