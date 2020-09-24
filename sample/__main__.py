from .api import HoxhuntApi
from .api import IncidentsIter

AUTH_TOKEN = ""
API_URL = "https://app.hoxhunt.dev/graphql-external"

if __name__ == '__main__':
    api = HoxhuntApi(auth_token=AUTH_TOKEN, api_url=API_URL)
    iter = IncidentsIter(api)
    print(next(iter))
    print(next(iter))
