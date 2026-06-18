
                                    # Matplot labels 
import numpy as np 
import matplotlib.pyplot as plt 


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title(" Fat loss")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()


# Either you can make a dictionary of specifications 
# or change labels specifications seperatly 


plt.xlabel('Average pulse ',fontname="Arial" ,size=200,color='hotpink')
plt.ylabel("Calorie Burn",color="hotpink",size=90,loc='bottom')
plt.title("New title",color='red')

plt.show()


# Now making a dict

dict1={"color":'red','family':'Arial','size':20}
dict2={"color":'hotpink','family':'Arial','size':20}

plt.xlabel('Average pulse ',fontdict=dict1)
plt.ylabel("Calorie Burn",fontdict=dict2)
plt.title("New title",color='red')

plt.show()