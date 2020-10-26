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


    def get(self, url: str, query_params: dict = {}, headers: dict = {}) -> dict:
        """ Makes a ``GET`` request to the specified url
        """
        return {}


    def post(self, url: str, query_params: dict = {}, body_params: dict = {}, headers: dict = {},
             return_headers: bool = False) -> dict:
        """ Makes a ``POST`` request to the specified url

        """
        return {}
