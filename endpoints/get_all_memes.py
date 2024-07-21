import os
import allure
import requests

base_url = 'http://167.172.172.115:52355/meme'
from endpoints.base_api import BaseApi

token = os.getenv('TOKEN')


class GetAllMemes(BaseApi):

    @allure.step('GetAllMemes')
    def get_all_memes(self):
        auth = token
        self.response = requests.request('GET', base_url, headers={
    'Authorization': auth,
})
        self.response_json = self.response.json()
        print(self.response_json)

    def get_memes_not_authorized(self):
        self.response = requests.request('GET', base_url)
        print(self.response)
