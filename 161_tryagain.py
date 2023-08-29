def get_info(id2find):
        result_f = open("surfing_data.csv")
        for line in result_f:
            s = {}
            (s['id'], s['name'], s['country'], s['average'], s['boardtype'], s['age']) = line.split(";")
#           print("debug is the for working")    
            if id2find == int(s['id']):
#               print("debug is the if working")
#               print("debug is " + str(id2find) + " working")
                return(s)
                result_f.close
#       print("testing if this comes up when i enter an unknown")
        return({})
        result_f.close()

a = 0
while (a < 10):
        try:
                lookupid = int(input("Enter the ID of the surfer! "))        
                surfer = get_info(lookupid)
                if surfer != {}:
                        print("ID:          " + surfer['id'])
                        print("Name:        " + surfer['name'])
                        print("Country:     " + surfer['country'])
                        print("Average:     " + surfer['average'])
                        print("Board type:  " + surfer['boardtype'])
                        print("Age:         " + surfer['age'])
                else:   
                        print("sorry, try again! That ID was not found as a surfer in our system")
        except:
                print("Stop putting letters in a numerical field!!")
