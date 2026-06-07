

                                    # Data Distribution 

'''
Data Distribution is a list of all possible values, and how often each value occurs.

Such lists are important when working with statistics and data science.

The random module offer methods that returns randomly generated data distributions.

'''



                                       # Random Distribution  

# It is a set of random numbers that following a certain probability 



 
import numpy as np 
from numpy import random 

x=random.choice([1,2,3,5,7],p=[0.0,0.2,0.6,0.1,0.1],size=(100))

print (x)


# Note : The sum of all probability should be one 
# Note : The value  one will never occure 


x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)


Python concepts + Libraries/#9 Python Library Numpy/#2 Numpy Random/#2 Data Distribution .py

