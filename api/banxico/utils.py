""" Utils for differents requests to banxico endpoints

Attributes:
    _logger(logging.Logger): The logger of this endpoints
"""
import re
import logging
from models.external import Request
from config import (
    BANXICO_TOKEN,
    BANXICO_URL,
    BANXICO_UDIS_SERIE,
    BANXICO_USD_TO_MXN_SERIE
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
        name = udis_response.get("bmx", {}).get("series", [])[0].get("titulo", "")
        dates = udis_response.get("bmx", {}).get("series", [])[0].get("datos", "")
        if dates:
            for date in dates:
                udis_values_per_day[date.get("fecha", "")] = float(date.get("dato"))

            max_udi_value = (max(dates, key=lambda x:float(x.get("dato", -1))))
            min_udi_value = (min(dates, key=lambda x:float(x.get("dato", -1))))
            average_udi = float(sum(float(d['dato']) for d in dates)) / len(dates)
            response= {
                "name": name,
                "average_udi_value": average_udi,
                "max_udi_value": {
                    "value": float(max_udi_value.get("dato", -1)),
                    "date": max_udi_value.get("fecha", -1)
                },
                "min_udi_value":{
                    "value": float(min_udi_value.get("dato", -1)),
                    "date": min_udi_value.get("fecha", -1)
                },
                "dates_udis": udis_values_per_day
            }

        return response
    else:
        return {}


def get_usd_mxn_serie(initial_date: str, end_date:str) -> dict:
    """ This function make a request to the banxico endpoint that returns the udis per days values
    Return:
        dict: Formated response with min, max, average and all values per day of udis.
    """

    url = f"{BANXICO_URL}/{BANXICO_USD_TO_MXN_SERIE}/datos/{initial_date}/{end_date}"
    usd_response = _request_handler.get(url, headers=_headers)
    usd_values_per_day = {}
    response = {}
    if usd_response:
        name = re.sub(' +', ' ', usd_response.get("bmx", {}).get("series", [])[0].get("titulo", ""))
        dates = usd_response.get("bmx", {}).get("series", [])[0].get("datos", "")
        if dates:
            for date in dates:
                usd_values_per_day[date.get("fecha", "")] = float(date.get("dato"))

            max_usd_value = (max(dates, key=lambda x:float(x.get("dato", -1))))
            min_usd_value = (min(dates, key=lambda x:float(x.get("dato", -1))))
            average_usd = float(sum(float(d['dato']) for d in dates)) / len(dates)
            response= {
                "name": name,
                "average_usd": average_usd,
                "max_usd_value": {
                    "value": float(max_usd_value.get("dato", -1)),
                    "date": max_usd_value.get("fecha", -1)
                },
                "min_usd_value":{
                    "value": float(min_usd_value.get("dato", -1)),
                    "date": min_usd_value.get("fecha", -1)
                },
                "dates": usd_values_per_day
            }

        return response
    else:
        return {}