s = {}
#line = "101;Johnny 'wave-boy' Jones; USA;8.32;Fish;21"

#(s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = line.split(";")

#print("ID:  " + s['id'])
#print("Name:  " + s['name'])
#print("Country:  " + s['country'])
#print("Average:  " + s['average'])
#print("Board type:  " + s['board'])
#print("Age:  " + s['age'])


def find_details(id2find):
    surfers_f = open("surfing_data.csv")
    s = {}
    #for each_line in surfers_f:
    #    (s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = each_line.split(";")
    for line in surfers_f:
        (eyedee, name, country, average, boardtype, age) = line.split(";")
        s[eyedee] = eyedee 
        s[name] = name
        s[country] = country
        s[average] = average
        s[boardtype] = boardtype
        s[age] = age
        if id2find == int(s['id']):
            surfers_f.close()
            return(s)
        surfers_f.close()
        return({})

lookup_id = int(input("Enter the ID of the surfer here: "))
surfer = find_details(lookup_id)
if surfer:
    print("ID:          " + surfer['id'])
    print("Name:        " + surfer['name'])
    print("Country:     " + surfer['country'])
    print("Average:     " + surfer['average'])
    print("Board type:  " + surfer['board'])
    print("Age:         " + surfer['age'])
