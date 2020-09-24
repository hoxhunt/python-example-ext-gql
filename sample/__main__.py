from .api import HoxhuntApi

AUTH_TOKEN = ""
API_URL = ""

if __name__ == '__main__':
    api = HoxhuntApi(auth_token=AUTH_TOKEN, api_url=API_URL)
    result = api.run_incidents_query()
    print(result)
