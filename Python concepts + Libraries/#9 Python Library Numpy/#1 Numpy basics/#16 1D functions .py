import numpy as np 


arr=np.array([1,5,2,4,88,10])

print(arr.argmax())# Print the index on which maximum value is preset 

print (arr.argmin()) # Print the index on which  the minimum value is present 


print(arr.argsort()) # Print the indeces at which placing elements will make it sorted


print(np.where(arr>20)) # Print index where value is greater the 20

# Same functions can be applied to 2D array

