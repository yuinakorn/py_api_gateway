import httpx

from dotenv import dotenv_values


config_env = dotenv_values(".env")


def get_status_all():
    url = f"{config_env['API_URL']}/get_all_client"
    response = httpx.get(url, headers={})
    result = response.json()
    
    return result


def get_status_by_hoscode(hoscode):
    # use httpx to get data from api
    url = f"{config_env['API_URL']}/query/status/{hoscode}"
    response = httpx.get(url, headers={})
    result = response.json()
    
    return result