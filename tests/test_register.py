import os
from jsonschema import validate
from reqres_api_tests.schemas.account import (
    register_successfully,
    register_unsuccessfully,
)


def test_register_successfully(api_client):

    payload = {
        "email": os.getenv('EMAIL'),
        "password": os.getenv('REGISTER_PASSWORD'),
    }

    response = api_client.request(
        method='POST', endpoint='/api/register', json_data=payload
    )
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=register_successfully)


def test_register_unsuccessfully(api_client):

    payload = {"email": os.getenv('EMAIL')}

    response = api_client.request(
        method='POST', endpoint='/api/register', json_data=payload
    )
    body = response.json()

    assert response.status_code == 400
    validate(body, schema=register_unsuccessfully)
