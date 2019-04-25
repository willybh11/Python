def sub_dictionary(): #now with lists!
    d = {

        "dict1":{
            "1-5":[1,2,3,4,5],
            "6-10":[6,7,8,9,10]
                },

        "dict2":{                       #this looks like this because
            "11-15":[11,12,13,14,15],   #of a sad attempt to make
            "15-20":[16,17,18,19,20]    #this look nicer :(
                }

        }

    print d["dict1"]
    print d["dict2"]

    for i in range(5): print d["dict1"]["1-5"]  [i]
    for i in range(5): print d["dict1"]["6-10"] [i]
    for i in range(5): print d["dict2"]["11-15"][i]
    for i in range(5): print d["dict2"]["15-20"][i]

sub_dictionary()
