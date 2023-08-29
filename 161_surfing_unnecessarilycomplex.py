s = {}
surfresults = open("surfing_data.csv")

for line in surfresults:
    (id, name, country, average, boardtype, age) = line.split(";")
    s[id] = id
    s[name] = name
    s[country] = country
    s[average] = average
    s[boardtype] = boardtype
    s[age] = age
    #, s['name'], s['country'], s['average'], s['boardtype'], s['age']) = line.split(";")
    
    
for each in s:
    print(each, s[each])

