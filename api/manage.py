""" Server run file
This file create the flask application and starts the server
"""
import os

from application import create_app
import config

debug = config.DEBUG
host = os.getenv('IP', '0.0.0.0')
port = int(os.getenv('PORT', 8080))

app = create_app(debug)