from endpoints.base_api import BaseApi
import os
import allure
import requests

base_url = 'http://167.172.172.115:52355/authorize'

token = os.getenv('TOKEN')


class CheckAuthorization(BaseApi):

    @allure.step('Check if auth with valid token')
    def check_auth_valid(self):
        self.response = requests.request('GET', f'{base_url}/{token}')

    def check_auth_no_token(self):
        self.response = requests.request('GET', base_url)
        print(self.response)

    def check_auth_incorrect_token(self):
        self.response = requests.request('GET', f'{base_url}/{'UJHKJ'}')
        print(self.response)
