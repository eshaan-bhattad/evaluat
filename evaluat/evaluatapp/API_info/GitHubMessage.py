import requests
import json



response = requests.get("https://api.github.com/repos/eshaan-bhattad/profiledplaylist/commits")

responseString = response.json()

x=-1

Dict = {}
for i in responseString:
    x += 1
    name = responseString[x]['author']['login']
    messages = responseString[x]['commit']['message']
    Dict[name] = messages







