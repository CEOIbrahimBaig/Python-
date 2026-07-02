import numpy as np 
import matplotlib.pyplot as plt 
from numpy import random 
import seaborn as sns


                                      #  Binomial Distribution 

'''
It shows the odds of getting a specific number of successes 
when you repeat an action a fixed number of times.

Binomial Distribution is a Discrete Distribution.

It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

It has three parameters:

n - number of trials.

p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).
or you can say success Rate 


size - The shape of the returned array.

'''

x= random.binomial(n=10,p=0.5,size=10)

print (x)



sns.displot(random.binomial(n=10, p=0.5, size=1000))

plt.show()


data={
    "Normal":random.normal(loc=50,size=100,scale=10),
    "Binomial":random.binomial(n=100,p=0.5,size=100)
}

sns.displot(data,kind="kde")

plt.show() #The graphs tell how much every prediction deviates from the mean (Average ) or peak



