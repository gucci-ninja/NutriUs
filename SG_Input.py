import json
from pprint import pprint

ingredients = []

# Open the file to read
with open('Scraper/recipes.json') as data_file:    
    data = json.load(data_file)
    
# Open the file to write
target = open("SG_Input2.txt", 'w')



for i in data:
    target.write(str(i["recipe"])) # Change to id or recipe
    for j in range(len(i["ingredients"])):
        target.write("," + i["ingredients"][j].encode('utf-8'))
    target.write("\n")
        #ingredients.append(i["ingredients"][j].encode('utf-8'))
        #print(i["id"])




target.close()
