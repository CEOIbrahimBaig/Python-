s= set()

s.add(20) # Adds a 20 int data type in set 
s.add(20.0)#  Adds a 20 Float  data type in set
s.add("20")#  Adds a 20 string data type in set 

#So I think answer  is 3 
print (len(s))


# The real answer is 2 Why ?
# Because 20.0 is equal to 20 so it give 2 as answer not 3 