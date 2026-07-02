import numpy as np 
import matplotlib.pyplot as plt 
from numpy import random 
import seaborn as sns


                                      #  Normal Distribution 


#It shows data that naturally clusters around a central average, 
#where most things are average and extremes are rare.


'''
The Normal Distribution is one of the most important distributions.


It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.

It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.

Use the random.normal() method to get a Normal Data Distribution.

It has three parameters:

loc - (Mean) where the peak of the bell exists.

scale - (Standard Deviation) how flat the graph distribution should be.

size - The shape of the returned array.'''


x=random.normal(size=(2,3))



print(x)



x=random.normal(size=(2,3),loc=1 ,scale=2)

# loc means the peak (mean)
# scale is how much you daviate from peak

print (x) 





                    # Visualisation of Normal Distribution



sns.displot(random.normal(size=1000) ,  kind="kde")


plt.show()


