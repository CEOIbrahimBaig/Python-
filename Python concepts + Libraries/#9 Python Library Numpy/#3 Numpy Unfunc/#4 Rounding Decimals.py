
                              # Rounding Decimals 

'''
There are primarily five ways of rounding off decimals in NumPy:

truncation
fix
rounding
floor
ceil

'''


                                #Truncation

'''Remove the decimals, and return the float number closest to zero.
 Use the trunc() and fix() functions.'''

import numpy as np 

arr=np.trunc([-3.11,3.11])

print(arr)



arr=np.fix([-3.11,3.11])

print(arr)


                            # Rounding 

''' It Rounds the present last decimal point such as 1.35 to 1.4  and 
if lower then 5 then nothing happens '''


new_arr=np.around([3.17,3.16]) # It will not give 3.2 bcz rounding is set to zero by default

print ("\n",new_arr) # Gives 3. , 3. as output 

new_arr=np.around([3.17,3.127],decimals=1)
print (new_arr)

new_arr=np.around([3.17,3.127],2) # It will not round it will just cut parts and show till 2 decimal

print (new_arr)


# Floor function round of the decimal to nearest lowest decimal 

arr = np.floor([-3.1666, 3.6667]) # Gives -4, 3 

print(arr)



# Ceil function round of the decimal to nearest highest decimal 


arr = np.ceil([-3.1666, 3.6667]) # Gives -3,4

print(arr)

