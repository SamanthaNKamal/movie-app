import requests
import json
import time

def AmazonPrime()
"""
This method will use the API to search the amazon prime streaming service.

Returns:
Search results for a specific movie or TV show

"""

result = input("Enter the name of a movie or TV show: ")
url = "https://streamzui-streamzui-v1.p.rapidapi.com/search"
"""
URL to the unofficial Amazom Prime Video API on Rapid API 
Paid for access for a maximum of 30,000 streams
No access to API after 30,000 streams

"""

querystring = {"Movie":"TV show"}

headers = {
'x-rapidapi-key': "54e93237a1msh975f4560b132a79p19bb2ajsn83d84344d274",
'x-rapidapi-host': "streamzui-streamzui-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

if __name__ == "__main__":
    AmazonPrime()
