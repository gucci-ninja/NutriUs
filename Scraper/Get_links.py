# Python code to read file with 20000 recipe links
# Package that allows xml files to read like json
import xmltodict

# Open the xml file so it can be formatted conveniently
with open('recipedetail.xml/recipedetail.xml') as links:
    pages = xmltodict.parse(links.read())

# Location for output file
target = open("Recipe_Links.txt", 'w')

# Loop through the link entries and write to file
for i in range(len(pages['urlset']['url'])):
    target.write(pages['urlset']['url'][i]['loc'])
    target.write("\n")
    
target.close()

