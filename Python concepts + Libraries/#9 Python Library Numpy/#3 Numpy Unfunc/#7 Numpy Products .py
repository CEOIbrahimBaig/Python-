
                              # Numpy Product

import numpy as np



arr = np.array([1, 2, 3, 4])

x = np.prod(arr) # Output : 24

print(x)


arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2]) # OUTPUT :40320

print(x)


                            # Product over axis 



arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)


                             # Commulative product 


'''

Cummulative product means taking the product partially.

E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

Perfom partial sum with the cumprod() function.


'''

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)