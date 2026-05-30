
import numpy as np 

 #You can use both the Tuple to create array or list to create numpy ARRAY 


#1 Numpy array with list 

arr = np.array([1,2,3,4])

print (arr )
print (type(arr))

#2 Numpy array with tupple 

abb =np.array((1,2,3,4))

print (abb)
print (type(abb))



'''Python lists are mutable, tuples are immutable.
When converted into a NumPy array, both become normal mutable NumPy arrays.

NumPy usually copies the data, so the original list/tuple type matters very little afterward.

Tuples are slightly faster and use a bit less memory in plain Python, but the difference 
becomes almost negligible once inside NumPy.

Lists are used more because they are easier for building and modifying datasets before conversion.

For AI and NumPy performance, using list vs tuple almost never creates a noticeable speed difference.'''