import numpy as np 

                                # Shape of an ARRAY 

'''It is the number of element within an array '''


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)   # 1st has 2 element (2 brackts ) ,2nd inner dimension has 4 Elements 

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)

