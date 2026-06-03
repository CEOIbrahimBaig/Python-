import numpy as np 

                               #Sorting Arrays
'''Sorting means putting elements in an ordered sequence.

Ordered sequence is any sequence that has an order corresponding to elements,
like numeric or alphabetical, ascending or descending.

The NumPy ndarray object has a function called sort(), that will sort a specified arra'''

# For integers 

arr=np.array([1,7,7,2,5,1,2])

print (np.sort(arr))


# For Strings it sort them alphabatically 

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))


# For a bool data-type  = It sort false ,true  as false =0 and true =1 


arr = np.array([True, False, True])

print(np.sort(arr))


                 # For 2D Array 

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))


