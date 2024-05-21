import json

import httpx

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
    # use httpx to get data from api
    url = f"{config_env['API_URL']}/query/status/{hoscode}"
    response = httpx.get(url, headers={})
    result = response.json()

    return result
