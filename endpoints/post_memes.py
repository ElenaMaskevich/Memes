import os
import requests
import allure
from endpoints.base_api import BaseApi
from endpoints.schemas import CreateMeme
# from api_tests_elena_maskevich.endpoints.schemas import CreatedObject

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

    @allure.step('Check response name')
    def check_response_name(self, name):
        return self.response_json['name'] == name