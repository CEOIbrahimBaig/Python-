

                          # Matplotlib Histograms 

'''

A histogram is a graph showing frequency distributions.

It is a graph showing the number of observations within each given interval.





'''


import matplotlib.pyplot as plt
import numpy as np


x = np.random.normal(170, 10, 250)

# It will geenrate 250 Numbers with main point 170 and about 68 percent digit lie in 
# daviation of 10 numbers 

plt.hist(x)
plt.show() 

