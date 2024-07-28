import os
import requests
import allure
from endpoints.base_api import BaseApi
from endpoints.schemas import CreateMeme

base_url = 'http://167.172.172.115:52355/meme'

token = os.getenv('TOKEN')
header = {'Authorization': token}


class PostCreateMeme(BaseApi):
    @allure.step('Create meme')
    def create_meme(self, payload):
        self.response = requests.post(
            base_url,
            json=payload,
            headers=header
        )
        self.response_json = self.response.json()
        print(self.response_json)
        self.data = CreateMeme(**self.response_json)

    @allure.step('Trying to create meme without auth')
    def create_meme_no_auth(self, payload):
        self.response = requests.post(
            base_url,
            json=payload,
        )

    def check_created_meme_by_id(self):
        meme_id = self.response.json()['id']
        print(f'meme id {meme_id}')
        self.response_meme = requests.get(
            f'{base_url}/{meme_id}',
            headers=header
        )
        self.meme_json = self.response_meme.json()
        return self.meme_json['id'] == meme_id

    @allure.step('Check response info')
    def check_response_info(self, info):
        return self.response_json['info'] == info

    @allure.step('Check response tags')
    def check_response_tags(self, tags):
        return self.response_json['tags'] == tags

    @allure.step('Check response text')
    def check_response_text(self, text):
        return self.response_json['text'] == text

    @allure.step('Check response updated by')
    def check_response_updated(self, updated_by):
        return self.response_json['updated_by'] == updated_by

    @allure.step('Check response url')
    def check_response_url(self, url):
        return self.response_json['url'] == url
