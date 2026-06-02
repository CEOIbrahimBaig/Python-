import numpy as np 

                                    # Numpy split 
# It is oppsite  of join , it split the array 

# np.split () = Only split in equal parts else give error 
# np.array_split() = Split array even if extra number left or less left 

arr=np.array([1,2,3,4,5,6,7,8,9])

new_arr=np.array_split(arr,4 )

# It will create equal 4 parts and print them 

print (new_arr)

# IF we perform unequal division then it split automatically in best possible equal parts

new_arr=np.array_split(arr,7)

print (new_arr)

# You can access the split part in following ways 
print("\n")
print(new_arr[0])
print(new_arr[1])
print(new_arr[2])




                                          # For 2D Array

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr) 

print("\n",newarr[1])


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)


# NOTE THAT THE vsplit(),hsplit,dsplit() work same but opposite to vstack(),hstack(),dstack()


