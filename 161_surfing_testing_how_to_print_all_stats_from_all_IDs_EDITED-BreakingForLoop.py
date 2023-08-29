s = {}
surfresults = open("surfing_data.csv")

# we need this variable to exit the for-loop to do a deeper analysis...
counter = 3;

for line in surfresults:
    (s['id'], s['name'], s['country'], s['average'], s['boardtype'], s['age']) = line.split(";")
    print("I just iterated ONE line from the CSV into the hash s") #if this prints more than once, I know the for loop is working and not just running once then dying
    if counter == 3:
        # we want to stop the for-loop after X iteration(s), X being the value of the counter variable set in line 5
        break

print(s)

print("why does this only print one ID's information rather than every ID's information??")
#why does this only print one ID?

for each in s.keys():
    print(s[each])
#why does this print aaron's rather than everyone's data?
