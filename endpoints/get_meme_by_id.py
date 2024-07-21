import os
import allure
import requests
from endpoints.base_api import BaseApi
token = os.getenv('TOKEN')


base_url = 'http://167.172.172.115:52355/meme'


class GetMemeById(BaseApi):

    @allure.step('GetMemeById')
    def get_meme_by_id(self, id):
        self.response = requests.request('GET', f'{base_url}/{id}', headers={
    'Authorization': token})
        self.response_json = self.response.json()


    @allure.step('Check id meme')
    def check_response_id(self, id):
        return self.response_json['id'] == id


    @allure.step('Trying to get meme without auth')
    def get_meme_not_auth(self, meme_id):
        self.response = requests.request('GET', f'{base_url}/{id}')
