import requests
import pytest
import os
from endpoints.post_authorize import Authorization
from endpoints.get_check_if_authorize import CheckAuthorization
from endpoints.get_all_memes import GetAllMemes
from endpoints.post_memes import PostCreateMeme
from endpoints.get_meme_by_id import GetMemeById
from endpoints.put_meme import PutMemeById
from endpoints.delete_memes import DeleteMeme
from tests.data import payloads


base_url = 'http://167.172.172.115:52355/meme'

project_root = os.path.dirname(os.path.dirname(__file__))
env_project = os.path.join(project_root, '.env')
token = os.getenv('TOKEN')


@pytest.fixture()
def check_authorize():
    return Authorization()


@pytest.fixture()
def check_token():
    return CheckAuthorization()


@pytest.fixture()
def create_meme():
    payload = {
            "info": {"test": "sdsd"},
            "tags": [
                "Some tag",
                "another tag"
            ],
            "text": "Some meme",
            "url": "www.testsetset.com"
        }
    create_meme = PostCreateMeme()
    create_meme.create_meme(payload=payload)
    meme_id = create_meme.response.json()['id']
    print(f'Created meme with id {meme_id}')
    yield meme_id
    deleted_meme=DeleteMeme()
    deleted_meme.delete_meme(meme_id)
    print(f'Deleted meme with id {meme_id}')



@pytest.fixture()
def get_all_memes():
    return GetAllMemes()


@pytest.fixture()
def create_new_meme():
    return PostCreateMeme()


@pytest.fixture()
def get_meme_by_id():
    return GetMemeById()


@pytest.fixture()
def put_meme_by_id():
    return PutMemeById()


@pytest.fixture()
def delete_meme_by_id():
    return DeleteMeme()
