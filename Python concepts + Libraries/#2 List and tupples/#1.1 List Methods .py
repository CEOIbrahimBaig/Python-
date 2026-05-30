

                                     # LIST CONCEPTS AND FUNCTIONS  

data=["Apple","Ibrahim","Hafsa",23,True,"Mehboob"]

print(data)

data.append("Ali Hassan")  # It insert a data at the end of list 

print (data)

numbers=[2,1,4,5,55,0,5]

# First method = .sort()
numbers.sort()
print(numbers)

# 2nd Method .reverse()

numbers.reverse()

print(numbers)

#3RD Method .insert(index,data) To insert at specific index 

numbers.insert(1,223)

print (numbers)

#4th Method .pop(index) To delete an element from the list and return the deleted value 

print(numbers.pop(1))# It returns the deleted value and delete the element from the list 

deleted_number=numbers.pop(2) # Storing the deleted number in the variable 

print (numbers)

print (deleted_number)

#5th method .remove(22) # It removes the entered data from the list 

numbers.remove (0)

print (numbers)


