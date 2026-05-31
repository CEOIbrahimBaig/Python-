


                                     #Reshaping arrays

'''Reshaping means changing the shape of an array.

The shape of an array is the number of elements in each dimension.

By reshaping we can add or remove dimensions or change number of elements in each dimension.'''




import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

arr2=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])

newarr=arr2.reshape(1,1,4,4)

print (newarr)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)


# You can not reshape in unequal way , the number of coulumns should be equal 

# WHILE  RESHAPING THE FUNCTION ALLOW YOU TO ALLOCATE UNKNOWN NUMBER OF ELEMENT TO ONE DIMENSION 
#FOR EXAMPLE 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1) # It automatically calculate proper number of elements 

print(newarr)


                   # FLATTENING ARRAY 

'''It means converting multi-dimensional array into single array , we can do it by following method '''

arr= np.array([
[
[1,2],
[4,5]
],
[
[7,9],
[2,3]
]

])

newarr=arr.reshape(-1)

print(newarr)

######## If you wrinte arr.reshape(6) It will arrange all the 6 elements in single list 


