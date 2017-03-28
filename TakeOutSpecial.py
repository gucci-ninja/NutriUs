

tofilter = open("UniqueIngredients.txt", 'r')
count = 0
for line in tofilter:
    if (u"\N{TRADE MARK SIGN}".encode('utf-8') in line) or (u"\N{REGISTERED SIGN}".encode('utf-8') in line) or (u"\N{COPYRIGHT SIGN}".encode('utf-8') in line):
        count = count + 1
        temp = []
        for charc in line:
            temp.append(charc)
            if (charc == u"\N{REGISTERED SIGN}".decode('utf-8')):
                print charc
                del temp[len(temp) - 1]
            ''.join(temp)
        print line
        

print count
        


#target = open("UniqueIngreFixed.txt", 'w')
#or (u'\N{REGISTERED SIGN}'.encode('ascii', 'ignore') in line) or (u'\N{COPYRIGHT SIGN}'.encode('ascii', 'ignore') in line)
