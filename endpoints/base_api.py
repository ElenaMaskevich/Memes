import allure
import requests


class BaseApi:
    response: requests.Response
    response_json: dict
    token: str
    response_meme: requests.Response
    meme_json: dict

    @allure.step('Check status code')
    def check_status_code_(self, code):
        return self.response.status_code == code
