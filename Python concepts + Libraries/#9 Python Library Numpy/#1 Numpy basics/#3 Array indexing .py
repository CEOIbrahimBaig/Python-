

                            #1 Printing element of 0D array 

import numpy as np 

arr= np.array(23)

print ( arr )


print ("\n")

                             #2 Printing an element from 1D Array 

arr_1D= np.array([1,2,3,45,6])

print (arr_1D[3]) # Print the element at third index 

# Adding elements of 1D array 

print (arr_1D[0]+arr_1D[1]) # Print the sum of 0th and 1st index 

print ("\n")


                           #3 2D array elements accessing 

arr_2D=np.array([

[1,3,55],
[44,55,77]

]) 

# Print 77 which is 2nd row third column 
# Indexing of row and column start from zero not one 


print (arr_2D[1,2])    # print (array_2D[row,column ]) 


# 3D Array Elements accessing 


array_3D =np.array([

[
[1,2,4],[2,4,5]
],
[
[2,9,5],[3,5,6]
]

])


# For Accessing 9 check which part it is in first or secound , then check column and row 

print(array_3D[1,0,1])

# print (array_3D[Part,row,column])




'''
Example Explained


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2]) prints the value 6.

And this is why:

The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6

'''


# NEGATIVE INDEXING CAN ALSO BE USED IN NUMPY 

neg_index_array=np.array([
[1,2,4],[4,5,6]
])

print ("The 2nd last element of 2nd row is ",neg_index_array[-1,-2]) # print 5 

