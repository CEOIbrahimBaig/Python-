

                          # Matplotlib Bars


import matplotlib.pyplot as plt
import numpy as np


x=np.array(["A","B","C","D"])
y=np.array([2,4,5,10])

plt.bar(x,y,color="Green",width=0.1) # To increase size of data-bar use width=


plt.show()

# To plot bars horizontally use plt.barh() instead of plt.bar()
# For plt.barh() use height= to increase size of data-bars

x=np.array(["A","B","C","D"])
y=np.array([2,4,5,10])

plt.barh(x,y,color="hotpink",height=0.01)

plt.show()
