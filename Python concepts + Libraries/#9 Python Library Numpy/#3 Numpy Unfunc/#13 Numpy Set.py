
                              # Numpy  Set 

'''

A set is a collection of well define distinct elements .


'''
import numpy as np

x=np.array([1,1,1,1,1,2,3,3,5,2,5,6,7])


abj=np.unique(x)

print (abj)



                            # 1 Dimensional Union   & Intersection 

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)




newarr = np.intersect1d(arr1, arr2, assume_unique=True)

# assume_unique is optional argument , Default value = True , It speed up the proccess 

print(newarr)

                        # 1-Dimesnional Difference 


newarr=np.setdiff1d(arr1,arr2)

print(newarr)

                         # 1-Dimensional Symmetric Difference 

''' It provides you the values which are not present in both set 
'''
newarr=np.setxor1d(arr1,arr2)

print (newarr)

