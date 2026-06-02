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


