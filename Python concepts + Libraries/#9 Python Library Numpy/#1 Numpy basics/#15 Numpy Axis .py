import numpy as np 


# 1D Array has only one axis = axis0

#2d Array has two axix ,axis0 and axis1 
'''
Axis0 = Row 
Axis 1 = Column 
'''

my_list=[
    [1,2],
    [3,4],
    [5,6]
]

arr=np.array(my_list)

print("The sum of columns are following ",arr.sum(axis=0))

print("The sum of all rows are following ",arr.sum(axis=1))



