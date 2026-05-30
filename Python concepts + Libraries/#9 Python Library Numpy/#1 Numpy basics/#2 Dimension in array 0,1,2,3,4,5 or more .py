
# ZERO DIMENSIONAL ARRAY 

# It contain only one digit , No ROWS and No Columns only one digit and zero dimension 

import numpy as np 

arr=np.array(12)  # Zero dimensional array 

print ("This is data in zero dimensional array ",arr)


#1D array  - Data is indexed in normal way 

abb=np.array([1,2,3,4,5])

print (abb)
print("\n")

#2D Array  - It contain rows and columns 

acc=np.array([
    [1,2],[2,3]
])

print(acc)
print("\n")

#3D Array 


arr_3D=np.array(

[
    [
[1,2],[3,4]

    ],
    [
[5,6],[7,8]
    ]
]

)

print(arr_3D)



# To check number of dimension an array has use following keyword 

print ("\n")

print (arr.ndim)
print (abb.ndim)
print (acc.ndim)
print (arr_3D.ndim)

# 5D array 


array_5D =np.array(  [1,2,3,4,5]    ,ndmin=5) #ndmin means number of dimensions 

print("\n")


print(array_5D)


print ("The number of dimension in array is ",array_5D.ndim)





