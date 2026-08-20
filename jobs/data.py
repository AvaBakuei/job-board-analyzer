import requests


def data_load() -> list:
    base_url = "https://www.arbeitnow.com/api/job-board-api"
    response = requests.get(base_url)
    data = response.json()
    return data["data"]
