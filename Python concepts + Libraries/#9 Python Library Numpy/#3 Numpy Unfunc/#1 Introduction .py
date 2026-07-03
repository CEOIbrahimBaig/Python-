
                                       # Unfunc 


'''

unfunc means universal functions  and they are  functions that  operate on ndarray 

'''

# Why use UNFUNC 

'''
unfunc is used to implement vectorization in numpy which is way faster then iteration over elements 


They also provide broadcasting & other methods like reduce  ,accumlate , They help for computation 

ufuncs also take additional arguments, like:

where boolean array or condition defining where the operations should take place.

dtype defining the return type of elements.

out output array where the return value should be copied.

'''

                                 # Vectorization
'''
Converting iterative statement into verctor based operation is called Vectorization     


''' 

# There are two  methods to add two list 

 #1st Without unfunc method 

list_1=[1,2,35,6]
list_2=[2,35,68,6]
z=[]

for i,j in zip(list_1,list_2):
    z.append(i+j)

print (z)



#2nd Method to do is it by unfunc 
import numpy as np 

z=np.add(list_1,list_2)

print ("\n",z)



