
                                # Random Number

'''

Random number does NOT mean a different number every time. Random means something that can not be 
predicted logically.
'''
                            # Pseudo Random and True Random
'''
Computers work on programs, and programs are definitive set of instructions. So it means there 
must be some algorithm to generate a random number as well.

If there is a program to generate random number it can be predicted, thus it is not truly random.

Random numbers generated through a generation algorithm are called pseudo random.

Can we make truly random numbers?

Yes. In order to generate a truly random number on our computers we need to get the random 
data from some outside source. This outside source is generally our keystrokes, mouse movements, 
data on network etc.

We do not need truly random numbers, unless it is related to security (e.g. encryption keys) or 
the basis of application is the randomness (e.g. Digital roulette wheels).
'''

import numpy as np

from numpy import random

x=random.randint(100)

print (x)


# For Random float values 

x=random.rand()

print (x)

# For Random Multiple values 


x=random.randint(100,size=5)# Generate an array of 5 random int 

print (x)


# For 2D Array use following 


arr=random.randint(100,size=(3,5)) # Print 3 rows  5 columns 2d array 

print (arr)

# For floats intead of int replace random.randint with random.rand()


# When random.randint(100 ) = one digit between 0 to 100 
# When random.rand (100) = 100 random floats are generated 
# For int you  need size for float you can write  directly 
                             
                                 # For float 

x=random.rand(5) # 5 Random float 
print (x)

x=random.rand(5,5) # 5 rows 5 column random float 

print ("\n",x)



                                    # Choice function ( )
'''It help you select randomly from the given materials ''' 


x =random.choice([1,2,3,4])

print(x)

x= random.choice([1,2,4,5,6],size=(3,2,2))
print (x)

print(x.dtype)


