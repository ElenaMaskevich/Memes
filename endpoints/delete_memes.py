import os

import requests
import allure
from endpoints.base_api import BaseApi

base_url = 'http://167.172.172.115:52355/meme'
token = os.getenv('TOKEN')
header = {'Authorization': token}


class DeleteMeme(BaseApi):
    @allure.step('Delete meme')
    def delete_meme(self, meme_id):
        self.response = requests.delete(
            url=f"{base_url}/{meme_id}", headers=header
        )
        print(self.response)

    @allure.step('Trying to get deleted meme')
    def get_deleted_meme(self, meme_id):
        self.response = requests.get(
            url=f"{base_url}/{meme_id}", headers=header
        )
        print(self.response)

    @allure.step('Trying to delete meme with incorrect auth')
    def delete_meme_incorrect_auth(self, meme_id):
        self.response = requests.delete(url=f"{base_url}/{meme_id}", headers={'Authorization': 'asd23'})
        print(self.response)
