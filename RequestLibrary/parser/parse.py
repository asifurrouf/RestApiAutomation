import json

from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)

pprint(data)

data["maps"][0]["id"]
data["masks"]["id"]
data["om_points"]