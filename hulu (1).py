import requests
import json

def  Hulu():
     """This method will search the Hulu API for the title of the movie or tv show (Simrat Kaur).
    
    Returns:
        The title of the movie or the tv show.
    """

    result = input("Enter in the Movie Title or TV Show:")
    url = "https://hulu1.p.rapidapi.com/search" + result

    querystring = {"type":"Movie","page":"1","title":"batman"}

    headers = {
        'x-rapidapi-key': "b08ebf0eb1msh1a42bdbfe0d3d70p138554jsn9e81d1deb388",
        'x-rapidapi-host': "hulu1.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    print(response.text)
    
    jsonResponse = response.json()

    for key, value in jsonResponse.items():
        print(jsonResponse["items"][0]["title"])

if __name__ == "__main__":
    Hulu()