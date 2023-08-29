#function to get info from CSV
def find_details(id2find):
    surfers_f = open("surfing_data.csv")
    for each_line in surfers_f:
        s = {}
        (s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = each_line.split(";")
        if id2find == int(s['id']):
            print("WE HAVE A MATCH!") #this is for debugging to tell me that the if condition actually ran
            surfers_f.close()
            return(s)
        else:
            print("WE DO NOT HAVE A MATCH!")
    surfers_f.close()
    return({})

#program begins!

#ask user for a surfer ID & assign it to lookup_id

x = 0

while x < 1:
    lookup_id = int(input("Enter the ID of the surfer here: "))

    #print info to screen
    surfer = find_details(lookup_id) 
    if surfer:
        print("ID:          " + surfer['id'])
        print("Name:        " + surfer['name'])
        print("Country:     " + surfer['country'])
        print("Average:     " + surfer['average'])
        print("Board type:  " + surfer['board'])
        print("Age:         " + surfer['age'])
    else:
        print("you got nothing")
