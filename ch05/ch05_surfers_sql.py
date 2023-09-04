import sqlite3

def get_info(id2find):

        db = sqlite3.connect("surfersDB.sdb") #connect to database
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute("select * from surfers")
        rows = cursor.fetchall()
        for row in rows:
                if row['id'] == id2find: # if the id inputted matches the id in the database
                    s = {} #make a hash 
                    s['id'] = str(row['id']) #assign the id/name/country/average/board/age from db to the hash
                    s['name'] = str(row['name'])
                    s['country'] = str(row['country'])
                    s['average'] = str(row['average'])
                    s['board'] = str(row['board'])
                    s['age'] = str(row['age'])
                    cursor.close()
                    return(s) #return the hash 
        cursor.close()    
        return({}) #otherwise, return nothing

a = 0
while (a < 10):    #keep allowing user to look up a new surfer by their ID
        try:
                lookupid = int(input("Enter the ID of the surfer! "))   #ask the user for a surfer's ID
                surfer = get_info(lookupid)                             #see if the surfer exists
                if surfer != {}:                                        #print the surfer's information if what was returned wasn't empty
                        print("ID:          " + surfer['id'])
                        print("Name:        " + surfer['name'])
                        print("Country:     " + surfer['country'])
                        print("Average:     " + surfer['average'])
                        print("Board type:  " + surfer['board'])
                        print("Age:         " + surfer['age'])
                else:                                                   #if the surfer doesn't exist, warn the user and allow them to try again
                        print("sorry, try again! That ID was not found as a surfer in our system!")
        except Exception as e:                                          #in the book, it never asks you to solve 
                print(repr(e))
                print("Stop putting letters in a numerical field!!")
cursor.close()
