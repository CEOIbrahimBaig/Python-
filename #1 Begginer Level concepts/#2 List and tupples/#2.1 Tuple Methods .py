
                                              #Tuple Methods 

a=(1,True ,"Baig ",23,33.5 ,"Hafsa")

print (a)



#1st .count() To know how many times a certain data come in the tuple 

# It returns the amount of time a value repeat in a tuple 

amount=a.count("Baig")

print (amount)

#2nd  .index() Tell first coming index of a certain data  , If not found then give error 

index=a.index("Hafsa")

print (index)

#3rd .sum() Print sum of all the digits 
numbers=(1,2,3)

sum=sum(numbers)

print (sum)

#4th Slicing - Breaking tupple but rememember it is not mutable so it updates the value into another 
# but dont change itself  

num=(1,2,3,4,5,6)
sliced_tuple=num[0:3]
print (sliced_tuple)

