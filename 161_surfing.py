s = {}
surfresults = open("surfing_data.csv")

for line in surfresults:
    (s['id'], s['name'], s['country'], s['average'], s['boardtype'], s['age']) = line.split(";")
    
    
for each in s:
    print(each, s[each])

