
                                       # Unfunc function Creation 


'''
To create your own ufunc, you have to define a function, like you do with normal functions
 in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

The frompyfunc() method takes the following arguments:

function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.


'''

import numpy as np

def my_add(x,y):
    return x+y


my_add=np.frompyfunc(my_add,2,1)

print(my_add([1,2],[2,4]))


# To check if a function is unfunc or not 
print (type(np.add))



# Another way to check is 

if type(np.add)=="np.unfunc":
    print("It is an unfunc function ")
else:
    print("It is not an unfunc function")

    