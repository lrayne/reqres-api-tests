import allure
from allure_commons.types import Severity
from jsonschema import validate
from reqres_api_tests.schemas.response.resources import (
    resources_list_retrieved,
    single_resource_info_retrieved,
)


@allure.severity(Severity.NORMAL)
@allure.suite('Ресурсы')
@allure.title('Получение ресурсов с уникальными id')
def test_all_the_resources_should_have_unique_id(api_client):

    response = api_client.request(method='GET', endpoint='/api/unknown')
    body = response.json()
    ids = [element['id'] for element in body['data']]

    assert response.status_code == 200
    assert body['total'] == 12
    assert list(set(ids)) == ids
    validate(body, schema=resources_list_retrieved)


@allure.severity(Severity.NORMAL)
@allure.suite('Ресурсы')
@allure.title('Получение ресурса по id')
def test_get_existing_resource_by_id(api_client):

    id = '2'

    response = api_client.request(method='GET', endpoint=f'/api/unknown/{id}')
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=single_resource_info_retrieved)


@allure.severity(Severity.MINOR)
@allure.suite('Ресурсы')
@allure.title('Получение не существующего ресурса по id')
def test_get_non_existing_resource_by_id(api_client):

    id = '23'

    response = api_client.request(method='GET', endpoint=f'/api/unknown/{id}')
    body = response.json()

    assert response.status_code == 404
    assert body == {}
