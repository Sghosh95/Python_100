#nested dictionary and list

## -*- coding: latin-1 -*-
travel_log={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Stutgart","Berlin"]
    
}
#print the dict
# print(travel_log)

#print Lille :
# print(travel_log["France"][1])

#######################big dictionary practice###########################
travel_log={
            "France":{
                "Cities_visited":["Paris","Lille","Dijon"],
                "Number_of_visits":8
                    },
            "Germany":{
                "Cities_visited":["Berlin","Hamberg","Stutgart"],
                "Number_of_visits":12
                    }
            }
            
#print the dictionary
print(travel_log)

#print Stutgart
print(travel_log["Germany"]["Cities_visited"][2])
