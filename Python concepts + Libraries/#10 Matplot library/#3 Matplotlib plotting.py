

                                          # Plotting

'''
    Plotting x and y points

The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.

''' 


import matplotlib.pyplot as plt 
import numpy as np 


# Plot x axis 1 to 8  and y Axis 3-10 


x_axis=np.array([1,8])
y_axis=np.array([3,10])


plt.plot(x_axis,y_axis)

plt.show()



                        # Plotting without a line and only a dot 

'''To plot only the markers, you can use shortcut string 
notation parameter 'o', which means 'rings'.'''


xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints,ypoints, 'o')
plt.show()

# For multiple points add data in array 


x3points=np.array([0,2,4,15])
y3points=np.array([0,1,2,15])

plt.plot(x3points,y3points,'o') # If you remove o then it will show connected lines 

plt.show()


                                # Default X Points 

# If we give Only one point /List it  takes all values of x as default points 

experimentpoint=np.array([0,1,2,15,16])

plt.plot(experimentpoint)
plt.show()

 # NOTE: YOU CAN NOT REPEAT SAME VALUES IN THE LIST 



