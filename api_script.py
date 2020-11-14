
""" This is a script for adding an API in json format."""
import requests
import json
from pprint import PrettyPrinter
pp = PrettyPrinter() #beautify the JSON output

jsonFile = requests.get("Place your API in here")

jsonObject = json.loads(jsonFile.content)
print(jsonObject["Title"])