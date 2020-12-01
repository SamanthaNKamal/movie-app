import requests

url = "https://netflix-unofficial.p.rapidapi.com/api/search"

headers = {
    'x-rapidapi-key': "979499eb08msh3664a876cdc17fcp17f3adjsnde10b912d78f",
    'x-rapidapi-host': "netflix-unofficial.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)