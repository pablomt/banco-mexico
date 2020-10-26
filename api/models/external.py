""" Requests model

This model handles the external requests
"""
import logging
import json
import requests


class Request:
    """ The class that create an instance of requests and allow
    the requests for external urls

    Attributes:
        logger(logging.Logger): The logger of the model
    """
    logger = logging.getLogger(__name__)

    def __init__(self):
        """ Initialization of the instance"""


    def get(self, url: str, query_params: dict = {}, headers: dict = {}, return_headers: bool = False) -> dict:
        """ Makes a ``GET`` request to the specified url
        """
        response = requests.get(url, params=query_params, headers=headers)

        if response.status_code < 200 or response.status_code >= 300:
            self.logger.error("The url returned a code %s",
                              response.status_code)
        else:
            self.logger.info("The request to url %s was successful", response.url)

            if return_headers:
                return response.headers

            try:
                return response.json()
            except json.JSONDecodeError:
                if response.text:
                    return response.text

                if response.content:
                    return response.content.decode("utf-8")

            self.logger.error("The response does not contain a valid payload from url %s", url)
            return {}

        return {}


    def post(self, url: str, query_params: dict = {}, body_params: dict = {}, headers: dict = {},
             return_headers: bool = False) -> dict:
        """ Makes a ``POST`` request to the specified url

        """
        response = requests.post(url, json=body_params, params=query_params, headers=headers)

        if response.status_code < 200 or response.status_code >= 300:
            self.logger.error("The url %s returned a code %s",
                              url,
                              response.status_code)

            return {}
        else:
            self.logger.info("The request to url %s was successful", response.url)

            if return_headers:
                return response.headers

            try:
                return response.json()
            except json.JSONDecodeError:
                if response.status_code == 204:
                    return { "response": "204 no content", "code": 204 }

                if response.text:
                    return response.text

                if response.content:
                    return response.content.decode("utf-8")

            self.logger.error("The response does not contain a valid payload")
            return {}

        return {}
