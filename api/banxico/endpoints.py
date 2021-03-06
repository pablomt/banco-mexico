""" Endpoints definition

This file contains all the endpoints for the Watson interactions

Attributes:
    logger(logging.Logger) - The logger of the utilities
"""
import logging
from flask import Blueprint, request
from flask_api import status
import datetime as dt

from . import utils

series_app = Blueprint('series_app', __name__)
logger = logging.getLogger(__name__)

@series_app.route('/get-udi-series', methods=['GET'])
def get_udies_series():
    """
    .. http:get:: /api/v1/get-udi-series

        Returns Udies values per day, max, min and average between a date range.

        **Example request**
            .. sourcecode:: http

                GET /api/v1/get-udi-series HTTP/1.1
                HOST: example.com

                PARAMS
                    "initial_date": 01-01-20202
                    "end_date": 25-10-20202

        **Example response**
            .. sourcecode:: http

                HTTP/1.1 200 OK
                Vary: Accept
                Content-Type: application/json

                {
                    "min_udi_value": 6.00,
                    "max_udi_value": 7.00,
                    "average_udi_value": 6.55,
                    "dates_udis": [
                        {
                            "date": "01/10/2020",
                            "value": "6.550290"
                        },
                    ]
                }

        :<json float min_value: The udi min value for specific range of date.
        :>json float max_value: The udi max value for specific range of date
        :<json float average: The udi average value for specific range of date
        :>json list dates: All the days with their own udi value
        :status 200: The dict of response returned
        :status 422: Wrong parameters on the body of the request
    """
    initial_date = request.args.get('initial_date', "2020-01-01")
    end_date = request.args.get('end_date', "2020-31-12")

    try:
        dt.datetime.strptime(initial_date, "%Y-%m-%d")
        dt.datetime.strptime(end_date, "%Y-%m-%d")
    except:
        return {"error": "Formato de fecha invalido: aaaa-dd-mm"}, 422

    response = utils.get_udis_series(initial_date, end_date)

    if response:
        return {'response': response}, status.HTTP_200_OK

    return {'response': 'Lo sentimos, no hay datos para las fechas proporcionadas.'}, status.HTTP_200_OK


@series_app.route('/get-usd-mxn', methods=['GET'])
def get_usd_mxn_serie():
    """
    .. http:get:: /api/v1/get-usd-mxn

        Returns USD in MXN values per day, max, min and average between a date range.

        **Example request**
            .. sourcecode:: http

                GET /api/v1/get-usd-mxn HTTP/1.1
                HOST: example.com

                PARAMS
                    "initial_date": 01-01-20202
                    "end_date": 25-10-20202

        **Example response**
            .. sourcecode:: http

                HTTP/1.1 200 OK
                Vary: Accept
                Content-Type: application/json

                {
                    "min_value": 6.00,
                    "max_value": 7.00,
                    "average": 6.55,
                    "dates": [
                        {
                            "date": "01/10/2020",
                            "value": "6.550290"
                        },
                    ]
                }

        :<json float min_value: The udi min value for specific range of date.
        :>json float max_value: The udi max value for specific range of date
        :<json float average: The udi average value for specific range of date
        :>json list dates: All the days with their own udi value
        :status 200: The dict of response returned
        :status 422: Wrong parameters on the body of the request
    """
    initial_date = request.args.get('initial_date', "2020-01-01")
    end_date = request.args.get('end_date', "2020-31-12")

    try:
        dt.datetime.strptime(initial_date, "%Y-%m-%d")
        dt.datetime.strptime(end_date, "%Y-%m-%d")
    except:
        return {"error": "Invalid Date format: aaaa-dd-mm"}, 422

    response = utils.get_usd_mxn_serie(initial_date, end_date)

    if response:
        return {'response': response}, status.HTTP_200_OK

    return {'response': 'Lo sentimos, no hay datos para las fechas proporcionadas.'}, status.HTTP_200_OK