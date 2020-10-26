""" Utils for differents requests to banxico endpoints

Attributes:
    _logger(logging.Logger): The logger of this endpoints
"""
import logging
from models.external import Request
from config import (
    BANXICO_TOKEN,
    BANXICO_URL,
    BANXICO_UDIS_SERIE
)

_logger = logging.getLogger(__name__)
_request_handler = Request()
_headers = {
    "Bmx-Token": BANXICO_TOKEN,
    "Content-Type": "application/json"
}

def get_udis_series(initial_date: str, end_date:str) -> dict:
    """ This function make a request to the banxico endpoint that returns the udis per days values
    Return:
        dict: Formated response with min, max, average and all values per day of udis.
    """

    url = f"{BANXICO_URL}/{BANXICO_UDIS_SERIE}/datos/{initial_date}/{end_date}"
    udis_response = _request_handler.get(url, headers=_headers)
    udis_values_per_day = {}
    response = {}
    if udis_response:
        dates = udis_response.get("bmx", {}).get("series", [])[0].get("datos", "")
        if dates:
            response["max_udi_value"] = max(dates, key=lambda x:x.get("dato", ""))
            response["min_udi_value"] = min(dates, key=lambda x:x.get("dato", ""))
            response["average_udi"] = float(sum(float(d['dato']) for d in dates)) / len(dates)
            for date in dates:
                udis_values_per_day[date.get("fecha", "")] = date.get("dato")
            response["dates"] = udis_values_per_day

        return response
    else:
        return {}