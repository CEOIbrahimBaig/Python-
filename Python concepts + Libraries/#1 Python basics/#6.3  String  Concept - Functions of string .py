
# You can never change a string , You can only create a new one using functions or update using functions 
name="Ali.hassan"

print(len(name)) # Tell the length of string 
print(name.endswith("an")) # Tell if  string end  with certain chars or not 
print (name.startswith("Ali")) # Tell if string start with certain chars or not 

print (name.capitalize()) # It capitalize first word of string 

index =name.find("hassan") # Will store value of index from where we can find the value

print (index)

name.replace("Ali","hassan") # It does not change the orignal name 
name=name.replace("Ali","hassan") #It WILL STORE THE UPDATED STRING INTO ORIGNAL STRING 
print(name)

text = "name=Ali Hassan"
key, sep,value = text.partition(" ")

print(key)    # name
print(value)  # Ali Hassan
