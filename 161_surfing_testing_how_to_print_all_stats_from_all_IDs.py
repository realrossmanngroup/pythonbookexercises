s = {}
surfresults = open("surfing_data.csv")

for line in surfresults:
    (s['id'], s['name'], s['country'], s['average'], s['boardtype'], s['age']) = line.split(";")
    print("I just iterated ONE line from the CSV into the hash s") #if this prints more than once, I know the for loop is working and not just running once then dying
    
    
print(s)

print("why does this only print one ID's information rather than every ID's information??")
#why does this only print one ID?

for each in s.keys():
    print(s[each])
#why does this print aaron's rather than everyone's data?
