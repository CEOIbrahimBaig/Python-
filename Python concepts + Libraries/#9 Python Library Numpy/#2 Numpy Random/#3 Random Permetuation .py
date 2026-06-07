
                                # Random Permetuation

'''
A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3]
 and vice-versa.

The NumPy Random module provides two methods for this: shuffle() and permutation().'''

import numpy as np 
from numpy import random 

arr=np.array([1,2,4,5,6])

random.shuffle(arr)   # Change the orignal array 

print (arr)


arr2=np.array([1,2,3,4,5,6])

print (random.permutation(arr2))  # It does not change the orignal array 
print (arr2)



