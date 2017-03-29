#Python code to create a list of dictionaries and store it in json file
import json
import re

unwanted = ["active", "liters", " s ", "divided", "finely ", "thinly sliced", "freshly", "jar", "chopped", "peeled", "cored", "for frying",
            "sliced", "grated", "dash", "ounces", "ounce", "cups", "cup", "teaspoons", "teaspoon", "tablespoons", "tablespoon", "deveined",
            "dry", "cleaned", "to taste", "water", "warm","cold", "hot", "minced", "packages", "shredded", "refrigerated", "halved", "and ",
            "pinch", "cloves", "separated", "mashed", "beaten", "pounds", "cubed","pint ", "large", "small", "package", "crumbled" "scoop",
            "seeded", "inch", "pieces", "piece", "millileter", "bottle", "degrees F", "degrees C", "melted","softened", "uncooked", "cooked",
            "undrained", "diced", "cut into strips", "frozen", "thawed", "pound", "halves", "can ", "dried", "reserved", "juiced",
            "or ", "prepared", "with peel", "peeled", "fluid", "gallon", "quartered", "cut ", " into ", "fresh", "thick ", "scrubbed",
            "lengthwise", "slices", "drained", "optional", "cubes", "as needed", "stems removed", "thirds", "diagonally", "sifted"]
# Create empty list
li = []
print("Making your json file")
with open("Recipes.txt") as f:
    for line in f:
        words = line.rstrip().split('!')
        ings = words[1:]
        for i in range(len(ings)):
            ings[i] = filter(lambda c: (not c.isdigit() and not (c=='/') and not (c==',') and not (c=='.') and not (c=='+') and not (c=='(') and not (c==')') and not (c=='-')), ings[i])
            for j in range(len(unwanted)):
                ings[i] = ings[i].replace(unwanted[j], "")
            ings[i] = re.sub('\s+', ' ', ings[i]).strip()
        ings = filter(None, ings) 

        d = { "recipe": words[0],
              "ingredients": ings
              }
        li.append(d)
        print(".")


with open("recipes.json", 'w') as ins:
    ins.write(json.dumps(li, sort_keys = False, indent=4, separators=(',',':')))
        
'''

[
  { "recipe": #####,
    "ingredients": [ ####,
                     ####,
                     ####
                    ]
  },
  
  { "recipe": #####,
    "ingredients": [ ####,
                     ####,
                     ####
                    ]
   }
]

'''
