import os
import requests
import allure
from endpoints.base_api import BaseApi
from endpoints.schemas import PutMeme

base_url = 'http://167.172.172.115:52355/meme'
token = os.getenv('TOKEN')
header = {'Authorization': token}


class PutMemeById(BaseApi):
    @allure.step('Put created meme')
    def put_meme(self, meme_id, payload):
        self.response = requests.put(
            url=f"{base_url}/{meme_id}",
            json=payload,
            headers=header
        )
        self.response_json = self.response.json()
        print(self.response_json)
        self.data = PutMeme(**self.response_json)

    @allure.step('Check response info')
    def check_response_info(self, info):
        return self.response_json['info'] == info

    @allure.step('Check response tags')
    def check_response_tags(self, tags):
        return self.response_json['tags'] == tags

    @allure.step('Check response text')
    def check_response_text(self, text):
        return self.response_json['text'] == text

    @allure.step('Trying put meme without auth')
    def put_meme_not_auth(self, meme_id, payload):
        self.response = requests.put(
            url=f"{base_url}/{meme_id}",
            json=payload,
        )
