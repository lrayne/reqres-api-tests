import os
import requests
from reqres_api_tests.utils import (
    request_logs,
    response_logs,
    request_attaching,
    response_attaching,
)


class ApiClient:

    def __init__(self):
        self.url = os.getenv('API_URL')
        self.session = requests.Session()

    def request(
        self,
        endpoint,
        method,
        data=None,
        params=None,
        json_data=None,
        allow_redirects=False,
    ):
        url = f'{self.url}{endpoint}'

        response = self.session.request(
            method,
            url,
            data=data,
            params=params,
            json=json_data,
            allow_redirects=allow_redirects,
        )

        request_logs(response)
        request_attaching(response)

        response_logs(response)
        response_attaching(response)

        return response
