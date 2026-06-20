

                          # Matplotlib Pie Charts 


import matplotlib.pyplot as plt
import numpy as np


y = np.array([35, 25, 25, 15])

label=np.array(["Apple","Banana","Fruit","Nothing"])

plt.pie(y,labels=label)
plt.show() 


'''
As you can see the pie chart draws one piece (called a wedge) for each value 
in the array (in this case [35, 25, 25, 15]).

By default the plotting of the first wedge starts from the x-axis and moves counterclockwise:

'''

# You can make some parts prominenet by explode= explode_quantity_list



y = np.array([35, 25, 25, 15])

label=np.array(["Apple","Banana","Fruit","Nothing"])

explodes=[0.3 ,0.0,0.0,0.8]

plt.pie(y,labels=label,explode=explodes,shadow=True)
plt.show() 



y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 



# Now Testing skill by making photo asked by gemini 




data=np.array([30,20,15,25])

labels_of_data=np.array(["Apple","Dates","Cherries","Bananas"])

color_of_data=np.array(["blue","red","green","orange"])

data_explode_limit=np.array([0.0,0.0,0.0,0.2])

plt.pie(data,labels=labels_of_data,colors=color_of_data,shadow=True,explode=data_explode_limit)
plt.title("Fruit Preference Survery Data ")

plt.show()