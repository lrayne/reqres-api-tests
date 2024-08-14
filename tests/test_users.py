import allure
from allure_commons.types import Severity
from jsonschema import validate
from reqres_api_tests.schemas.response.users import (
    user_created,
    user_updated,
    single_user_info_retrieved,
    users_list_retrieved,
)
from reqres_api_tests.schemas.request.users import user_info


@allure.severity(Severity.NORMAL)
@allure.suite('Пользователи')
@allure.step('Получение пользователей с уникальными id')
def test_all_the_users_should_have_unique_id(api_client):

    response = api_client.request(method='GET', endpoint='/api/users')
    body = response.json()
    ids = [element['id'] for element in body['data']]

    assert response.status_code == 200
    assert body['total'] == 12
    assert list(set(ids)) == ids
    validate(body, schema=users_list_retrieved)


@allure.severity(Severity.MINOR)
@allure.suite('Пользователи')
@allure.step('Получение пользователей с delay')
def test_get_all_the_users_with_delay(api_client):

    response = api_client.request(
        method='GET', endpoint='/api/users', params={'delay': '3'}
    )
    body = response.json()

    assert response.status_code == 200
    assert response.elapsed.total_seconds() <= 3.500000
    validate(body, schema=users_list_retrieved)


@allure.severity(Severity.NORMAL)
@allure.suite('Пользователи')
@allure.step('Получение cуществующего пользователя по id')
def test_get_existing_user_by_id(api_client):

    id = '2'

    response = api_client.request(method='GET', endpoint=f'/api/users/{id}')
    body = response.json()

    assert response.status_code == 200
    validate(body, schema=single_user_info_retrieved)


@allure.severity(Severity.MINOR)
@allure.suite('Пользователи')
@allure.step('Получение не существуюшего пользователя по id')
def test_get_non_existent_user_by_id(api_client):

    id = '23'

    response = api_client.request(method='GET', endpoint=f'/api/users/{id}')
    body = response.json()

    assert response.status_code == 404
    assert body == {}


@allure.severity(Severity.CRITICAL)
@allure.suite('Пользователи')
@allure.step('Успешное создание пользователя')
def test_create_user_successfully(api_client):

    name = 'morpheus'
    job = 'leader'
    payload = {'name': name, 'job': job}

    validate(payload, user_info)
    response = api_client.request(
        method='POST', endpoint='/api/users', json_data=payload
    )
    body = response.json()

    assert response.status_code == 201
    assert body['name'] == name
    assert body['job'] == job
    validate(body, schema=user_created)


@allure.severity(Severity.MINOR)
@allure.suite('Пользователи')
@allure.step('Успешное создание пользователя без указания места работы')
def test_create_user_without_job_successfully(api_client):

    name = 'morpheus'
    payload = {'name': name}

    validate(payload, user_info)
    response = api_client.request(
        method='POST', endpoint='/api/users', json_data=payload
    )
    body = response.json()

    assert response.status_code == 201
    assert body['name'] == name
    validate(body, schema=user_created)


@allure.severity(Severity.MINOR)
@allure.suite('Пользователи')
@allure.step('Успешное создание пользователя без имени')
def test_create_user_without_name_successfully(api_client):

    job = 'leader'
    payload = {'job': job}

    validate(payload, user_info)
    response = api_client.request(
        method='POST', endpoint='/api/users', json_data=payload
    )
    body = response.json()

    assert response.status_code == 201
    assert body['job'] == job
    validate(body, schema=user_created)


@allure.severity(Severity.MINOR)
@allure.suite('Пользователи')
@allure.step('Успешное создание пользователя без переданных атрибутов')
def test_create_user_without_provided_attributes_successfully(api_client):

    response = api_client.request(method='POST', endpoint='/api/users', json_data={})
    body = response.json()

    assert response.status_code == 201
    validate(body, schema=user_created)


@allure.severity(Severity.MINOR)
@allure.suite('Пользователи')
@allure.step('Успешное создание пользователя с custom атрибутом')
def test_create_user_with_custom_provided_attribute_successfully(api_client):

    value_of_custom_attribute = 'value'
    payload = {'myCustomAttribute': value_of_custom_attribute}

    response = api_client.request(
        method='POST', endpoint='/api/users', json_data=payload
    )
    body = response.json()

    assert response.status_code == 201
    assert body['myCustomAttribute'] == value_of_custom_attribute
    validate(body, schema=user_created)


@allure.severity(Severity.NORMAL)
@allure.suite('Пользователи')
@allure.step('Обновление информации о пользователе')
def test_update_user_info(api_client):

    name = 'john'
    job = 'co-leader'
    id = '2'
    payload = {'name': name, 'job': job}

    response = api_client.request(
        method='PUT', endpoint=f'/api/users/{id}', json_data=payload
    )
    body = response.json()

    assert response.status_code == 200
    assert body['name'] == name
    assert body['job'] == job
    validate(body, schema=user_updated)


@allure.severity(Severity.NORMAL)
@allure.suite('Пользователи')
@allure.step('Частичное обновление информации о пользователе')
def test_partial_update_user_info(api_client):

    job = 'co-leader'
    id = '2'
    payload = {'job': job}

    response = api_client.request(
        method='PATCH', endpoint=f'/api/users/{id}', json_data=payload
    )
    body = response.json()

    assert response.status_code == 200
    assert body['job'] == job
    validate(body, schema=user_updated)


@allure.severity(Severity.NORMAL)
@allure.suite('Пользователи')
@allure.step('Удаление пользователя')
def test_delete_user(api_client):

    id = '2'

    response = api_client.request(method='DELETE', endpoint=f'/api/users/{id}')

    assert response.status_code == 204
