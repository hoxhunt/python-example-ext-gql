from .api import HoxhuntApi
from .api import IncidentsIter
import os

AUTH_TOKEN = os.getenv('HOXHUNT_AUTH_TOKEN')
API_URL = "https://app.hoxhunt.com/graphql-external"

if __name__ == '__main__':
    api = HoxhuntApi(auth_token=AUTH_TOKEN, api_url=API_URL)
    iter = IncidentsIter(api)
    print(next(iter))
    print(next(iter))
