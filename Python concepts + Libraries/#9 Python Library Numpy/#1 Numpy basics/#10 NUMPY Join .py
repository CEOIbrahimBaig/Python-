import numpy as np 

                                 #   Joining NumPy Arrays


'''Joining means putting contents of two or more arrays in a single array.

In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

We pass a sequence of arrays that we want to join to the concatenate() function, 
along with the axis. If axis is not explicitly passed, it is taken as 0.'''

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)


First_arr2D=np.array([[1,2,3],[4,5,6]])
Secound_arr2D=np.array([[7,8,9],[10,11,12]])

new_arr2D=np.concatenate((First_arr2D,Secound_arr2D))

print(new_arr2D)


# Default axis=0 = IN rows form concatinate 
# Axis can be changed to 1 which  mean Horizontal concatination 
# Zero mean vertical concatination 


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]



 # Stack function also does the same thing 

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Stacking along a new axis (axis=1)
arr = np.stack((arr1, arr2), axis=1)
print(arr)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]


# Horizontal stacking 

arr=np.hstack((arr1,arr2))
print (arr)

# Print 1,2,3,4,5,6 

# Vertical stacking 

arr=np.vstack((arr1,arr2))

print(arr) # Print  1,2,3 
          #         4,5,6


# bstack() it also do vertical stacking but make a 3d array 

arr=np.dstack((arr1,arr2))
print (arr)

# Print vertical stack but with 3d array 