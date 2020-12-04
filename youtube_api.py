
import requests
import json

result = input("Enter in the Movie Title or TV Show:")
url = "https://youtube-search1.p.rapidapi.com/" + result

headers = {
    'x-rapidapi-key': "3d2fbbd54bmshbbccc15fd8196c7p11c1aejsn36237f19f62b",
    'x-rapidapi-host': "youtube-search1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
jsonResponse = response.json()

for key, value in jsonResponse.items():
    print(jsonResponse["items"][0]["title"])