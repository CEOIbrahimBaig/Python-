 

import numpy as np 

'''
Slicing arrays
Slicing in python means taking elements from one given index to another given index.

We pass slice instead of index like this: [start:end].

We can also define the step, like this: [start:end:step].

If we don't pass start its considered 0

If we don't pass end its considered length of array in that dimension

If we don't pass step its considered 1

'''

arr=np.array([1,2,3,4,5,6])

print (arr[1:5]) # It wil print from index 1 to 4 as 5th is end 


# For  printing from fixed index to end 

print ("\n")

print (arr[1:]) # Print from 2 to end 

print ("\n")

print(arr[:3])# Print from start to 2nd index 


arr2 = np.array([1,2,3,4,5,6])

print(arr2[1:7:2] )# print 2 and 4 



# You can skip the first two elements and write only third one as shown below 

print (arr2 [::2])# Print every 2nd element 1,3,5 

#2D Array slicing 

Array2d =np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])

print (Array2d[1,::2]) # Print 7,9,11 

#To print both lists 3rd element use following method 

print (Array2d[0:2,2]) # e.g print (array2d [row,column])

#To print for Both rows every 2nd element 

print ("\n")
print (Array2d[0:2,0:7:2]) # Print 1,3,5,7,9,11


# I did mistake her as I wrote like  print(array2d[0:2,0:7,2])
# while correct way to write it as   print(array2d[0:2,0:7:2])  : instead of "," comma 


arr3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])


#Make a code to print every 2nd element from all blocks 

print (arr3d[0:3,0:3,0:3:2])

# Print 11 from 3Darray 

print (arr3d[1,1,1])  

