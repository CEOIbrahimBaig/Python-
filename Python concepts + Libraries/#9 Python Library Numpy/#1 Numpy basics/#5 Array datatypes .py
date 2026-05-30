
'''
Data Types in Python
By default Python have these data types:

strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
integer - used to represent integer numbers. e.g. -1, -2, -3
float - used to represent real numbers. e.g. 1.2, 42.42
boolean - used to represent True or False.
complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j
Data Types in NumPy
NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float = Help to store complex digits e.g 5.1j + 2.6 j   Only j variable allowed 

m - timedelta - For range of time 

t = np.timedelta64(3, 'h')
print(t)

Output:

3 hours


M - datetime  - For specific time 
O - object = Store int ,string ,multiple datatype
S - string
U - unicode string = A string  which can store different  languages as well as emojis 
it is advance or upgraded version of string 

V - fixed chunk of memory for other type ( void )= No intrepreted datatype
'''



import numpy as np 



arr=np.array([-1,2,3,4,5,6])

print (type(arr)) # Tell you the date type of whole varirable 

print (arr.dtype)# Tell you the data type of elements inside variable 

ab=np.array([1,'2'])
print(ab.dtype)



# We can also assign fixed datatype to any array 