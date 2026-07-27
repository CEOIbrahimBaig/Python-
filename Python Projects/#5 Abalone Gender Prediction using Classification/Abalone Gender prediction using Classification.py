
import numpy as np 
import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier



# Import Dataset 

columns=[
    "Gender",
    "Length",
    "Diameter",
    "Height",
    "Whole_weight",
    "Shucked_weight",
    "Viscera_weight",
    "Shell_weight",
    "Rings"
]

dataset=pd.read_csv(r"C:\Python learning\Python Projects\#5 Abalone Gender Prediction using Classification\abalone.csv",names=columns)



# Split target and input 

X=dataset[[  "Length",
    "Diameter",
    "Height",
    "Whole_weight",
    "Shucked_weight",
    "Viscera_weight",
    "Shell_weight",
    "Rings"
    ]]

int_gender=[]

for i in dataset["Gender"]:
    if i=="M":
        int_gender.append(1)
    elif i=="F":
        int_gender.append(2)
    else:
        int_gender.append(3)


Target=int_gender

# Train model 

model=KNeighborsClassifier()


model.fit(X,Target)



# Now  predict 

print("\nPlease enter the details of the abalone:")

length = float(input("Length: "))
diameter = float(input("Diameter: "))
height = float(input("Height: "))
whole_weight = float(input("Whole weight: "))
shucked_weight = float(input("Shucked weight: "))
viscera_weight = float(input("Viscera weight: "))
shell_weight = float(input("Shell weight: "))
rings = int(input("Rings: "))


user_data = pd.DataFrame([[length, diameter, height, whole_weight, shucked_weight, viscera_weight, shell_weight, rings]])

prediction=model.predict(user_data)

if(prediction[0]==1):
    print("It is male ")
elif(prediction[0]==2):
    print("It is  Female")
else :
    print("It is infant")