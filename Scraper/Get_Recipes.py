# Python scraper to get create a json file with recipes and ingredients
import urllib2
from bs4 import BeautifulSoup

target = open("Recipes.txt", 'a')
target.write('\n')
count = 0

# open the text file with links
with open("Recipe_Links.txt") as ins:
    for link in ins:
        target.write(link.rstrip('\n'))
        # open the page
        page = urllib2.urlopen(link)

        # String input for page
        source = page.read()
        
        # make it pretty
        pretty_source = BeautifulSoup(source, 'html.parser')
        
        ingredients = pretty_source.find_all('span', class_='recipe-ingred_txt added')
        for i in range(len(ingredients)):
            try:
                target.write("!"+pretty_source.findAll("span", class_='recipe-ingred_txt added')[i].string)
            except UnicodeEncodeError:
                pass
        target.write("\n")
        count+=1
        print(count)
        
target.close()




#ingredient = filter(lambda c: (not c.isdigit()) and not c == ('/'), s)


