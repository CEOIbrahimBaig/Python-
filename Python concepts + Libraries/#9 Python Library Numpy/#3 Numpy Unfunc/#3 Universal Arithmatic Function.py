
                              # Arithmatic Universal Function 


import numpy as np

arr1=np.array([1,2,5])
arr2=np.array([3,4,8])

# We could have used simple arithmatic function wihtout  numpy but
# with numpy we are able to apply where function on arthimatic functions and it is fast then normaml 

new=arr1+arr2 # This is slow + we can't use Conditional Arithmatic here (where function basically )


print (new)   


# Using numpy library 

# For  ADDITION with NUMPY 

new_added_arary=np.where(arr1>2,np.add(arr1,arr2),arr1) 
#1st Argument = Condition
#2nd Argument = What to return if condition is True
#3rd Argument = What to retunrn if condition is False 
print  (new_added_arary)


# For SUBTRACTION with NUMPY 

new_subtracted_array=np.where(arr2>4,np.subtract(arr1,arr2),arr1)

print ("\n",new_subtracted_array)

# For Multiplication with Numpy 

new_multiplied_array=np.where(arr2>4,np.multiply(arr1,arr2),arr1)

print ("\n",new_multiplied_array)


# For Conditional Division By Numpy 



new_divided_array=np.where(arr2>4,np.divide(arr1,arr2),arr1)

print ("\n",new_divided_array)


# For condition Power applying with Numpy 


new_solved_array=np.where(arr2>4,np.power(arr1,arr2),arr1)

print ("\n",new_solved_array)


# For getting conditional Remainder from Numpy


# Both the remainder() and mode() give remainder after dividing 1st Argument with 2nd 

new_solved_array=np.where(arr2>4,np.remainder(arr1,arr2),arr1)

print ("\n",new_solved_array)


# For getting both remainder and quotient use this 


new_solved_array=np.where(arr2>4,np.divmod(arr1,arr2),arr1)

print ("\n",new_solved_array)



# To create condition Absolute use following abs () of absolute function 


new_solved_array=np.where(arr2>0,np.abs(arr1,arr2),arr1)

print ("\n",new_solved_array)

