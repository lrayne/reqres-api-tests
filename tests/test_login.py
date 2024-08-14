from allure_commons.types import Severity
from jsonschema import validate
from reqres_api_tests.schemas.response.account import (
    logged_in_successfully,
    failed_to_log_in,
)
from reqres_api_tests.schemas.request.account import credentials
import os
import allure


@allure.severity(Severity.CRITICAL)
@allure.suite('Аккаунт')
@allure.title('Авторизация')
def test_login_successfully(api_client):

    payload = {"email": os.getenv('EMAIL'), "password": os.getenv('LOGIN_PASSWORD')}

    validate(payload, credentials)
    response = api_client.request(
        method='POST', endpoint='/api/login', json_data=payload
    )
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=logged_in_successfully)


@allure.severity(Severity.MINOR)
@allure.suite('Аккаунт')
@allure.title('Авторизация без указания пароля')
def test_login_unsuccessfully(api_client):

    payload = {"email": os.getenv('EMAIL')}

    response = api_client.request(
        method='POST', endpoint='/api/login', json_data=payload
    )
    body = response.json()

    assert response.status_code == 400
    assert body['error'] == 'Missing password'
    validate(body, schema=failed_to_log_in)
