""" Health Endpoint Definition

Api health status check

"""
import logging
from flask import Blueprint
from flask_api import status

health_app = Blueprint('health_app', __name__)


@health_app.route('/health', methods=['GET'])
def health():
    """
    .. http:health:: /api/v1/health

        This endpoint check the health of the api.

        **Example request**
            .. sourcecode:: http

                GET /health HTTP/1.1
                HOST: example.com
                ACCEPT: application/json

        **Example response**
            .. sourcecode:: http

                HTTP/1.1 200 OK
                Vary: Accept
                Content-Type: application/json

                {
                    "status": "OK"
                }

        :reqheader Content-Type: application/json
        :>json string status: The status of the request it could be Healthy
        :status 200: OK. Status Healthy.
    """
    return {"status": "OK"}, status.HTTP_200_OK
