import os

import allure
import requests

import dotenv
from dotenv import set_key
from endpoints.base_api import BaseApi
from tests.data import payloads


dotenv.load_dotenv()

base_url = 'http://167.172.172.115:52355/authorize'

project_root = os.path.dirname(os.path.dirname(__file__))
env_project = os.path.join(project_root, '.env')
print(project_root)
print(env_project)


class Authorization(BaseApi):

    @allure.step('Authorization')
    def check_authorize(self):
        token = os.getenv('TOKEN')
        self.response = requests.get(f'{base_url}/{token}')
        status_code = self.response.status_code
        if status_code != 200:
            self.response = requests.post(
                base_url, json=payloads.payload_authorize
            )
            print(self.response)
            self.token = self.response.json()['token']
            print(self.token)
            self.token = self.response.json()['token']
            set_key(env_project, "TOKEN", self.token)

    def invalid_authorize(self):
        self.response = requests.post(base_url, json='')
        print(self.response.status_code)

