import os
import allure
from allure_commons.types import Severity
from jsonschema import validate
from reqres_api_tests.schemas.response.account import (
    registerged_successfully,
    failed_to_register,
)
from reqres_api_tests.schemas.request.account import credentials


@allure.severity(Severity.CRITICAL)
@allure.suite('Аккаунт')
@allure.title('Регистрация')
def test_register_successfully(api_client):

    payload = {
        "email": os.getenv('EMAIL'),
        "password": os.getenv('REGISTER_PASSWORD'),
    }

    validate(payload, credentials)
    response = api_client.request(
        method='POST', endpoint='/api/register', json_data=payload
    )
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=registerged_successfully)


@allure.severity(Severity.MINOR)
@allure.suite('Аккаунт')
@allure.title('Регистрация без указания пароля')
def test_register_unsuccessfully(api_client):

    payload = {"email": os.getenv('EMAIL')}

    response = api_client.request(
        method='POST', endpoint='/api/register', json_data=payload
    )
    body = response.json()

    assert response.status_code == 400
    validate(body, schema=failed_to_register)
