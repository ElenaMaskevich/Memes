from tests.data import payloads
from conftest import (check_authorize, create_meme, get_all_memes, create_new_meme, get_meme_by_id,
                      put_meme_by_id, delete_meme_by_id)


def test_all_memes(get_all_memes, check_authorize):
    get_all_memes.get_all_memes()
    assert get_all_memes.check_status_code_(200)
    assert get_all_memes.check_len_memes(1)


def test_no_memes_if_no_auth(get_all_memes, check_authorize):
    get_all_memes.get_memes_not_authorized()
    assert get_all_memes.check_status_code_(401)


def test_not_possible_create_meme_if_no_auth(create_new_meme):
    create_new_meme.create_meme_no_auth(payloads.payload_create_meme)
    assert create_new_meme.check_status_code_(401)


def test_create_new_meme(create_new_meme):
    create_new_meme.create_meme(payloads.payload_create_meme)
    assert create_new_meme.check_status_code_(200)
    assert create_new_meme.check_created_meme_by_id()
    assert create_new_meme.check_response_info(payloads.payload_create_meme['info'])
    assert create_new_meme.check_response_tags(payloads.payload_create_meme['tags'])
    assert create_new_meme.check_response_text(payloads.payload_create_meme['text'])
    assert create_new_meme.check_response_url(payloads.payload_create_meme['url'])


def test_not_possible_get_meme_by_id_if_no_auth(create_meme, get_meme_by_id):
    get_meme_by_id.get_meme_not_auth(create_meme)
    assert get_meme_by_id.check_status_code_(401)


def test_get_meme_by_id(create_meme, get_meme_by_id):
    get_meme_by_id.get_meme_by_id(create_meme)
    assert get_meme_by_id.check_status_code_(200)
    assert get_meme_by_id.check_response_id(create_meme)


def test_not_possilbe_update_meme_if_no_auth(create_meme, put_meme_by_id):
    payload = payloads.payload_put_meme
    payload['id'] = create_meme
    put_meme_by_id.put_meme_not_auth(create_meme, payload)
    assert put_meme_by_id.check_status_code_(401)


def test_update_meme(create_meme, put_meme_by_id):
    payload = payloads.payload_put_meme
    payload['id'] = create_meme
    put_meme_by_id.put_meme(create_meme, payload)
    assert put_meme_by_id.check_status_code_(200)
    assert put_meme_by_id.check_response_text(payloads.payload_put_meme['text'])
    assert put_meme_by_id.check_response_info(payloads.payload_put_meme['info'])
    assert put_meme_by_id.check_response_tags(payloads.payload_put_meme['tags'])


def test_not_possible_delete_meme_if_no_auth(create_meme, delete_meme_by_id):
    delete_meme_by_id.delete_meme_incorrect_auth(create_meme)
    assert delete_meme_by_id.check_status_code_(401)


def test_delete_meme(create_meme, delete_meme_by_id):
    delete_meme_by_id.delete_meme(create_meme)
    assert delete_meme_by_id.check_status_code_(200)
    delete_meme_by_id.get_deleted_meme(create_meme)
    assert delete_meme_by_id.check_status_code_(404)
