
import numpy as np 


                              #The Difference Between Copy and View

'''The main difference between a copy and a view of an array is that the copy is a new array, 
and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, 
and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array,
and any changes made to the original array will affect the view.'''


arr=np.array([1,2,3,4,5,6])

arr_copy=arr.copy()

arr[0]=42 # The arr changes but it's copy doesn't 

print (arr)
print (arr_copy)

arr_view=arr.view()

arr[0]=42 # The arr changes and so it's view 

print (arr)
print (arr_view)



arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)  # Print none as it does not  own data 
print(y.base)  # Print values as it own's it's data 

