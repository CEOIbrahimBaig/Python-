# Iteration means viewing or accessing each of the element in a set,list,tuple,array e.t.c

import numpy as np 

                            # For one Dimensional Array 

arr=np.array([1,2,3,5,6])


for x in arr : 
    print (x)


                        #  For 2D Array 

arr2D=np.array([
  [1,2,3,4],
  [1,5,6,7]

])

for x in arr2D: 
    print (x)


# If you want to print it in linear way  use following method for 2D ARRAY 

print ("\n")

for x in arr2D :
    for y in x : 
        print (y)


                                   # For 3D Array 

arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr3D:
  print(x)


  
# If you want to print it in linear way  use following method for 3D ARRAY 

for x in arr3D : 
    for y in x: 
        for z in y: 
            print (z)



# Instead of making so many loops we can use a function np.nditer (arr)


for x in np.nditer(arr3D): 
    print (x)



                     #Iterating Array With Different Data Types
'''We can use op_dtypes argument and pass it the expected datatype to change the datatype of 
elements while iterating.

NumPy does not change the data type of the element in-place (where the element is in array) 
so it needs some other space to perform this action, that extra space is called buffer, and in 
order to enable it in nditer() we pass flags=['buffered'].

'''


# It Only change data-type of array while it is in loop for fast calculations 
# It does not effect the real array 


for x in np.nditer(arr3D,flags=["buffered"],op_dtypes=["S"]):
    print (arr3D.dtype)
    print (x)
       

arr2d=np.array([
    [1,2,4],
    [5,6,7]
])

for x in np.nditer(arr2D[:, ::2]): # Print all rows and columns but skipping every 2nd element 
    print (x)

   



                  # Iteration with showing index = ndenumerate() 
                        
print("\n")

for index,x in np.ndenumerate(arr3D):
     print (index,x)


