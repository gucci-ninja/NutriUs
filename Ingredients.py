import json
from pprint import pprint

with open('ingredients.json') as data_file:    
    data = json.load(data_file)
count = 0
for i in data["tags"]:
    pprint(i["name"])


