import numpy as np 

# np.where () Return the indexes that match the given value or values 

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)


# To find even number 

even_index=np.where(arr%2==0)

print (even_index)


# For odd 


odd_index=np.where(arr%2==1)

print (odd_index)


                            # np.searchsorted(arr,value) 
'''
# Give us the index at which a particular value should be inserted for a sorted array  
# Search in BST FORM AND IS MADE FOR SORTED ARRAYS 
# Default search method is from left to right '''

arr = np.array([6,  8, 9,10])

x = np.searchsorted(arr, 7)

print(x) # Print 1 

# We can also search from right to left

index=np.searchsorted(arr,7,side='right')

print (index) # print 2 




# For Multiple value insertion position finding use following method 


indexes =np.searchsorted(arr,[1,2,12])

print(indexes)