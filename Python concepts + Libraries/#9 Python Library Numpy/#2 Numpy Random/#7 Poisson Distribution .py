import numpy as np 
import matplotlib.pyplot as plt 
from numpy import random 
import seaborn as sns


                                      # Poisson   Distribution 

'''

It estimates how many times an event can happen in a specified time. e.g. 
If someone eats twice a day what is the probability he will eat thrice?

It has two parameters:

lam - rate or known number of occurrences e.g. 2 for above problem.

size - The shape of the returned array.


'''

x=random.poisson(lam=2,size=10)  # lam =number of occurances (Average ) 

print (x)



sns.displot(random.poisson(lam=2, size=1000))

plt.show()