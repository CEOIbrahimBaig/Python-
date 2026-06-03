import numpy as np 


                               #  Filtering Arrays


'''Getting some elements out of an existing array and creating a new array out of them is called 
filtering.

In NumPy, you filter an array using a boolean index list.'''



#1 Boolean index list filtering 

bol_list=np.array([True,False,True,False])

arr=np.array([41,44,43,42])

new_arr=arr[bol_list] # It will store only indexes that has True Stored 

print(new_arr) 


# In the above example we hardcoded true or false but we can also use our own filter method 

arr=np.array([41,44,43,42])

filter_arr=[]  # Empty one 

# We are creating filter method which filter element above 42 


for element in arr : 
    if element>=42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)


new_array=arr[filter_arr]

print(new_array)



# Now creating  for even numbers  

arr=np.array([41,44,43,42])

filter_arr=[]  # Empty one 

# We are creating filter method which filter element above 42 


for element in arr : 
    if element%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)


new_array=arr[filter_arr]

print(new_array)


#Numpy provide us with a direct method also 

arr=np.array([41,44,43,42])

filter_arr=arr>=42

new_arr=arr[filter_arr]

print(filter_arr)
print (new_arr)



# Same can be done for the other example of even and odd 


arr=np.array([41,44,43,42])

filter_arr=arr%2==0

new_arr=arr[filter_arr]

print(filter_arr)
print (new_arr)