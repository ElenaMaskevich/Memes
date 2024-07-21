import allure
import pytest
from tests.data import payloads
from data.payloads import payload_create_meme
from conftest import (check_authorize, check_token, create_meme, get_all_memes, create_new_meme, get_meme_by_id,
                      put_meme_by_id, delete_meme_by_id)


def test_authorization(check_authorize):
    check_authorize.check_authorize()
    assert check_authorize.check_status_code_(200)
    check_authorize.invalid_authorize()
    assert check_authorize.check_status_code_(400)


def test_valid_token(check_token):
    check_token.check_auth_valid()
    assert check_token.check_status_code_(200)
    check_token.check_auth_no_token()
    assert check_token.check_status_code_(405)
    check_token.check_auth_incorrect_token()
    assert check_token.check_status_code_(404)


def test_all_memes(get_all_memes, check_authorize):
    check_authorize.check_authorize()
    get_all_memes.get_all_memes()
    assert get_all_memes.check_status_code_(200)
    assert get_all_memes.check_len_memes(1)
    get_all_memes.get_memes_not_authorized()
    assert get_all_memes.check_status_code_(401)


def test_create_new_meme(create_new_meme):
    create_new_meme.create_meme_no_auth(payloads.payload_create_meme)
    assert create_new_meme.check_status_code_(401)
    create_new_meme.create_meme(payloads.payload_create_meme)
    assert create_new_meme.check_status_code_(200)
    assert create_new_meme.check_created_meme_by_id()


def test_get_meme_by_id(create_meme, get_meme_by_id):
    get_meme_by_id.get_meme_not_auth(create_meme)
    assert get_meme_by_id.check_status_code_(401)
    get_meme_by_id.get_meme_by_id(create_meme)
    assert get_meme_by_id.check_status_code_(200)
    assert get_meme_by_id.check_response_id(create_meme)


def test_update_meme(create_meme, put_meme_by_id):
    payload = payloads.payload_put_meme
    payload['id'] = create_meme
    put_meme_by_id.put_meme_not_auth(create_meme, payload)
    assert put_meme_by_id.check_status_code_(401)
    put_meme_by_id.put_meme(create_meme, payload)
    assert put_meme_by_id.check_status_code_(200)
    assert put_meme_by_id.check_response_text('updated meme')


def test_delete_meme(create_meme, delete_meme_by_id):
    delete_meme_by_id.delete_meme_incorrect_auth(create_meme)
    assert delete_meme_by_id.check_status_code_(401)
    delete_meme_by_id.delete_meme(create_meme)
    assert delete_meme_by_id.check_status_code_(200)
    delete_meme_by_id.get_deleted_meme(create_meme)
    assert delete_meme_by_id.check_status_code_(404)
