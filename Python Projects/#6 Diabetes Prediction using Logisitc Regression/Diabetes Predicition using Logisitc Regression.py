
import numpy as np 
import pandas as pd 




# Import Dataset 

dataset=pd.read_csv(r"C:\Python learning\Python Projects\#6 Diabetes Prediction using Logisitc Regression\diabetes_dataset.csv")


print(dataset.keys())

mapping={
   
    "Physical_Activity_Level":{"Low":2,"Moderate":1,"High":0},
    "Alcohol_Consumption":{"None":0,"Moderate":1,"Heavy":2},
    "Smoking_Status":{"Never":0,"Former":1,"Current":2}
}

dataset=dataset.replace(mapping) # Mapping is done  according  to intesity leading to Diabetes

# Using One hot encoding to find Respective data 

'''' "Sex":{"Female":0,"Male":1},
    "Ethnicity":{"White":0,"Asian":1,"Black":2,"Hispanic":3},'''
