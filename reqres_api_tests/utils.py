import json
import logging
import allure
from allure_commons.types import AttachmentType
from requests import Response


def request_logs(response: Response):
    logging.info('Request: ' + response.request.url)
    logging.info('Request method: ' + response.request.method)
    logging.info('Request headers: ' + str(response.request.headers))
    if response.request.body:
        logging.info('INFO Request body: ' + str(response.request.body.decode('UTF-8')))


def response_logs(response: Response):
    logging.info('Response code: ' + str(response.status_code))
    logging.info('Response headers: ' + str(response.headers))
    if response.text:
        logging.info('INFO Response body: ' + response.text)


def request_attaching(response: Response):

    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    allure.attach(
        body=response.request.method, name="Method", attachment_type=AttachmentType.TEXT
    )
    allure.attach(
        body=json.dumps(dict(response.request.headers), indent=4),
        name="Request headers",
        attachment_type=AttachmentType.JSON,
    )

    if response.request.body:
        allure.attach(
            body=json.dumps(
                response.request.body.decode('UTF-8'), indent=4, ensure_ascii=True
            ),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )


def response_attaching(response: Response):

    allure.attach(
        body=str(response.status_code), name="Code", attachment_type=AttachmentType.TEXT
    )
    allure.attach(
        body=json.dumps(dict(response.request.headers), indent=4),
        name="Response headers",
        attachment_type=AttachmentType.JSON,
    )
    allure.attach(
        body=json.dumps(dict(response.cookies), indent=4),
        name="Cookies",
        attachment_type=AttachmentType.JSON,
    )

    if response.text:
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
