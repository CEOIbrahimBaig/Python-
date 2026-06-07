


                                        # Displot
'''It stands for a distributed plot 

It takes array input and plot a curve corresponding to distribution of points in array 

''' 


import matplotlib.pyplot as plt
import seaborn as sns


sns.displot([1,2,3,4,5,6])

sns.displot([1,2,3,4,5],kind="kde")

plt.show()