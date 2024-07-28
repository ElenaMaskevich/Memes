from conftest import (check_authorize, check_token)


def test_authorization(check_authorize):
    check_authorize.check_authorize()
    assert check_authorize.check_status_code_(200)


def test_invalid_authorization(check_authorize):
    check_authorize.invalid_authorize()
    assert check_authorize.check_status_code_(400)


def test_valid_token(check_token):
    check_token.check_auth_valid()
    assert check_token.check_status_code_(200)


def test_auth_with_invalid_token(check_token):
    check_token.check_auth_no_token()
    assert check_token.check_status_code_(405)
    check_token.check_auth_incorrect_token()
    assert check_token.check_status_code_(404)