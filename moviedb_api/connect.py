import requests
import os
import pprint
import pandas as pd
from conf import api_key_v3, api_key_v4

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
file_name = os.path.join(BASE_DIR, 'data.csv')
# HTTP Request Methods
"""
GET -> Getting Data
POST -> Add/Update
PATCH
PUT
DELETE

"""
# What is our endpoint (or url)

# What is the http method that we need?


"""

261207
Engpoint
GET
/movie/{movie_id}
'https://api.themoviedb.org/3/movie/550?api_key=51926fd69a18f404064693bdfc64872e'
"""
movie_id = 500
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
endpoint_path = f'/search/movie'
search_query = 'The matrix'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key_v3}&query={search_query}'
# header = {
#     "Authorization": "Bearer " + api_key_v4,
#     'Content-Type': 'application/json;charset=utf-8'
# }

r = requests.get(endpoint)
data = r.json()
print(data.keys())
movie_id = set()
# pprint.pprint(data["results"])
if r.status_code in range(200, 299):
    results = data["results"]
    for result in results:
        _id = result["id"]
        movie_id.add(_id)
movie_data = []
for movie in movie_id:
    movie_id = 500
    api_version = 3
    api_base_url = f'https://api.themoviedb.org/{api_version}'
    endpoint_path = f'/search/movie'
    search_query = 'The matrix'
    endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key_v3}&query={search_query}'
    r = requests.get(endpoint)
    data = r.json()
    movie_data.append(data)

df = pd.DataFrame(movie_data)
df.to_csv(file_name, index=False)
