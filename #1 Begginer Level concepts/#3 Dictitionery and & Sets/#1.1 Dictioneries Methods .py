data= {
 "Hafsa":100,
 "Ibrahim":98,
 "Ali":88,
 True:"Mehboob"
}

# 1st Method  .items() Print a tupple of whole data in decs_items 

print (data,"\n")# Print data in simple form

print(data.items(),"\n") # Print data in form tupple in a variable dict_items 

#2nd Methods .keys() Print all key values for a dictionery in variable dict_keys 

print (data.keys(),"\n")

#3rd Methods .values() Print all key values for a dictionery in variable dict_values 

print (data.values())

#4th Method .update() Update the present data in dictionery
#                     Also can be used to Add new data in dictionery 

data.update({"Harry":99,"Hafsa":100}) # The absent data is updated and new one is addded 

print (data)

#5th Method .get() Return the key 

print (data.get("HafSa")) # Does  not give error if absent key is entered , print null

print (data["Hafsa"]) # Give error if key is absent 


#6th Method .len( ) To get length of dictionery 

print(len(data))


# For printing empty dictionery 

s={
    
}
