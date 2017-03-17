import json
from pprint import pprint

ingredients = []

with open('recipes.json') as data_file:    
    data = json.load(data_file)
count = 0
for i in data:
    for j in range(len(i["ingredients"])):
        ingredients.append(i["ingredients"][j].encode('utf-8'))
        #print(i["id"])

#print(count)
print(ingredients[3])

ingredients_unique = []

for i in range(len(ingredients)):
    if ingredients[i] not in ingredients_unique:
        ingredients_unique.append(ingredients[i])
        
#ingredients_unique = set(ingredients)

print(len(ingredients_unique))

#with open("Unique_Ingredients", 'wb') as outfile:
 #   json.dump(ingredients_unique, outfile)



