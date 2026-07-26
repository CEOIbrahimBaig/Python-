
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

dataset=pd.read_csv(r"C:\Python learning\Python Projects\#5 Abalone Gender Prediction using Classification\ablone.csv",names=columns)



# Split target and input 

input=dataset[[  "Length",
    "Diameter",
    "Height",
    "Whole_weight",
    "Shucked_weight",
    "Viscera_weight",
    "Shell_weight",
    "Rings"
    ]]

Target=dataset["Gender"]


# Train model 

model=KNeighborsClassifier()


model.fit(input,Target)



# Now  predict 

prediction_detail=input(print("Please Enter the details of abalone to Know its Gender"))


