

                                # Matplot  lines 

'''
You can use the keyword argument linestyle, or shorter ls, 
to change the style of the plotted line:

OR You can just change struct while in the markers shape string 
'''


import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

'''
Shorter Syntax
The line style can be written in a shorter syntax:

linestyle can be written as ls.

dotted can be written as :.

dashed can be written as --.

'''


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r') # You can use color = or just c =
plt.show()


 # For changing width of line 


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5') # lw= or linewidth=  
plt.show()


                                       #Multiple Lines
'''You can plot as many lines as you like by simply adding more plt.plot() functions:'''



y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1) # Write seprately for two lines if you want default x axis 
plt.plot(y2)

plt.show()


# In case if you know y and x axis for both lines then following method is useful .


x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()




