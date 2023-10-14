import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])

# print(json.dumps(response.json(), indent = 2))

o = response.json()

for items in o["results"]:
    print(items["trackName"])