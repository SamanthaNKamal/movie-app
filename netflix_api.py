import requests

result = input("Enter in the Movie Title or TV Show:")
url = "https://youtube-search3.p.rapidapi.com/get_keywords_video/v1"
payload = f"region=us&keywords=%5B%22s{result}_the_movie%202%22%5D&language=en"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "979499eb08msh3664a876cdc17fcp17f3adjsnde10b912d78f",
    'x-rapidapi-host': "youtube-search3.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)


