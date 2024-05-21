import json

import httpx

import urllib.request
import urllib.error

from dotenv import dotenv_values

config_env = dotenv_values(".env")


def get_status_all():
    url = f"{config_env['API_URL']}/get_all_client"
    response = httpx.get(url, headers={})
    res = response.text
    data = json.loads(res)

    # Assuming data is a list of dictionaries, iterate and remove the 'check_visit' key
    for item in data:
        item.pop('check_visit', None)  # Use None to avoid KeyError if the key doesn't exist

    result = data

    return result


def get_status_by_hoscode(hoscode):
    try:
        # Use httpx to get data from API
        url = f"{config_env['API_URL']}/query/status/{hoscode}"
        request = httpx.Request('GET', url)
        response = httpx.get(url, headers={}, timeout=6.0)  # Set a timeout value
        response.raise_for_status()  # Raise an exception for HTTP errors
        result = response.json()
        return result

    except httpx.ReadTimeout:
        return {"status_code": 408, "error": "Request Timeout"}
    except httpx.HTTPStatusError as http_err:
        result = {"status_code": 400, "error": f"HTTP error occurred: {http_err}"}
    except httpx.RequestError as req_err:
        result = {"status_code": 400, "error": f"Request error occurred: {req_err}"}
    except Exception as err:
        result = {"status_code": 500, "error": f"An unexpected error occurred: {err}"}

    return result
