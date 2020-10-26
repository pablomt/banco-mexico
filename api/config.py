""" Configuration Load file

This file loads all the env variables needed.
"""
import os
import logging
import json

LOGGER = logging.getLogger(__name__)

if os.path.exists('.env'):
    LOGGER.info("Using .env file")
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())

# Flask environment
DEBUG = os.environ.get("DEBUG", True)
SECRET = os.environ.get("SECRET", "xxxxxx")

# Split each origin in a list
ORIGINS = (os.environ.get("ORIGINS", "*")).split(",")


# Banco de México Variables and Endpoints
BANXICO_TOKEN = os.environ.get("BANXICO_TOKEN", "")
BANXICO_URL = os.environ.get("BANXICO_URL", "")
BANXICO_UDIS_SERIE = os.environ.get("UDIS_SERIE", "")
BANXICO_USD_TO_MXN_SERIE = os.environ.get("BANXICO_USD_TO_MXN_SERIE", "")