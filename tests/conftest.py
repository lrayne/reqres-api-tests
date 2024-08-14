import pytest
from reqres_api_tests.client import ApiClient
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=False)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=False)
def api_client(load_env):
    client = ApiClient()
    return client
