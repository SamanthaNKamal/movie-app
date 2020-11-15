import requests
import json

from pprint import PrettyPrinter 
pp = PrettyPrinter() 


jsonFile = requests.get(

url = "https://hulu1.p.rapidapi.com/new"

querystring = {"Type":"Movie","days":"20","page":"1"}

headers = {
    'x-rapidapi-key': "SIGN-UP-FOR-KEY",
    'x-rapidapi-host': "hulu1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
)

print(response.text)

jsonObject = json.loads(jsonFile.content)

print(jsonObject["Batman"])
