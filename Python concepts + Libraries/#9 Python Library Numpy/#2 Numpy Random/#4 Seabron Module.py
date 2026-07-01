import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

sns.displot([0,1,2,3,4,5],bins=3)

# Bins are basically how many bars will be created .
# The values in the list are basically X axis values .

plt.show()
'''


A Real-World Example: Sorting Apples
Imagine you have 100 apples of all different weights, ranging from 100 grams to 200 grams.
 To make a histogram, you might set up 5 physical boxes (bins) on the floor:

Bin 1: 100g to 120g

Bin 2: 121g to 140g

Bin 3: 141g to 160g

Bin 4: 161g to 180g

Bin 5: 181g to 200g

You weigh each apple and drop it into its matching box.

The "Bin Width" is 20 grams (the size of each interval).

The "Bin Count" is how many apples end up in each box. The height of the bar on 
your chart represents this count.'''

#Plotting a Displot Without the Histogram


sns.displot([0,1,2,4,5],kind="kde") # It will create line instead of histogram


plt.show()