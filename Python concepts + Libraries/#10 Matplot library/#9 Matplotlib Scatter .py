

                          # Matplotlib Scatter 


import matplotlib.pyplot as plt
import numpy as np



x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.xlabel("Car Age")
plt.ylabel("Car Speed")
plt.title("Cars Analysis")
plt.show()





#day one, the age and speed of 13 cars
day_1_age = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
day_1_speed = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(day_1_age,day_1_speed,color='black')



#day two, the age and speed of 15 cars:
day_2_age = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
day_2_speed = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(day_2_age,day_2_speed,color="hotpink")


plt.xlabel("Car Age")
plt.ylabel("Car Speed")
plt.title("Cars Analysis")




plt.show()



# Or you can assign different  color to each point by making array 


car_age=np.array([12,22,55,66,100])
car_speed=np.array([100,700,220,100,50])

# Creating an array of colors to give to each data-point 

colors=np.array(["hotpink","blue","green","Black","red"])

# An array for size of each data-point 

sizes = np.array([20,50,100,200,500]) 


# Alpha is used for  transparency of each data-points
plt.scatter(car_age,car_speed,c=colors,s=sizes,alpha=0.5) # You have  to  use  c= not color= if using an array 
plt.xlabel("Car Age")
plt.ylabel("Car Speed")
plt.title("Car Analyzing")
plt.show()


# For assigning  colors to each data point you can alsoo use colormap 


# Note give color array in int and the specific int of an index will give specific color 
# according to the corresponding map int color 

#The function used in such case is cmap = 

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
plt.show()



