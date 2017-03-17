import json

with open('./dataset/recipes.json') as data_file:    
    recipes = json.load(data_file)

for recipe in recipes:
    numIngredients = len(recipe["ingredients"])
    
    recipe["numIngredients"] = numIngredients


recipes.sort(key=lambda k: k["numIngredients"])

with open('./dataset/NewRecipes.json', 'w') as f:
    json.dump(recipes, f)
