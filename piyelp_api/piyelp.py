import requests
import pandas as pd
import json
from config import api_key

url = 'https://api.yelp.com/v3/businesses/search'
header = {
    'Authorization': 'Bearer ' + api_key
}
params = {
    'term': 'restaurant',
    'location': 'NYC'
}
response = requests.get(url, headers=header, params=params)
data = response.json()
businesses = data["businesses"]
result = businesses[0]
if len(result) > 0:
    print(businesses[0].keys())
    busines_review = set()
    for business in businesses:
        # name = business["name"]
        # rating = business["rating"]
        review_count = business["review_count"]
        busines_review.add(review_count)
        # print(name, rating, review_count)
    print(list(busines_review))

rating_data = []
for review in busines_review:
    url = 'https://api.yelp.com/v3/businesses/search'
    header = {
        'Authorization': 'Bearer ' + api_key
    }
    params = {
        'term': 'restaurant',
        'location': 'NYC'
    }
    response = requests.get(url, headers=header, params=params)
    if response.status_code in range(200, 299):
        data = response.json()
        rating_data.append(data)


df = pd.DataFrame(rating_data)
df.to_csv("piyelp_api/reviews.csv", index=False)
