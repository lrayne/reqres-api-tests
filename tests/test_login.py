from jsonschema import validate
from reqres_api_tests.schemas.account import (
    login_successfully,
    login_unsuccessfully,
)
import os


def test_login_successfully(api_client):

    payload = {"email": os.getenv('EMAIL'), "password": os.getenv('LOGIN_PASSWORD')}

    response = api_client.request(
        method='POST', endpoint='/api/login', json_data=payload
    )
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=login_successfully)


def test_login_unsuccessfully(api_client):

    payload = {"email": os.getenv('EMAIL')}

    response = api_client.request(
        method='POST', endpoint='/api/login', json_data=payload
    )
    body = response.json()

    assert response.status_code == 400
    assert body['error'] == 'Missing password'
    validate(body, schema=login_unsuccessfully)
