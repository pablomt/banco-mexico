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

udis_serie_app = Blueprint('udis_serie_app', __name__)
logger = logging.getLogger(__name__)

@udis_serie_app.route('/getUdiSeries', methods=['GET'])
def get_udies_series():
    """
    .. http:get:: /api/v1/getUdiSeries

        Returns Udies values per day, max, min and average between a date range.

        **Example request**
            .. sourcecode:: http

                GET /api/v1/getUdiSeries HTTP/1.1
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
                    "average": "6.55",
                    "dates": [
                        {
                            "date": "01/10/2020",
                            "value": "6.550290"
                        },
                    ]
                }

        :<json string country_code: The contry code from the user
        :>json int    id: The city ID
        :<json string name: city name
        :>json string country_code: country code
        :>json string region_name: region name (federative state)
        :status 200: The dict of response returned
        :status 204: Session ID expired or empty response from cinepolis api
        :status 400: Wrong headers on the request
        :status 422: Wrong parameters on the body of the request
        :status 503: There was an internal error, review logs for more information
    """
    initial_date = request.args.get('initial_date', "2020-01-01")
    end_date = request.args.get('end_date', "2020-31-12")

    try:
        dt.datetime.strptime(initial_date, "%Y-%m-%d")
        dt.datetime.strptime(end_date, "%Y-%m-%d")
    except:
        return {"error": "Invalid Date format: aaaa-dd-mm"}, status.HTTP_400_BAD_REQUEST

    response = utils.get_udis_series(initial_date, end_date)

    if response:
        return {'response': response}, status.HTTP_200_OK

    return {'response': 'Lo sentimos, no hay datos para las fechas proporcionadas.'}, status.HTTP_200_OK