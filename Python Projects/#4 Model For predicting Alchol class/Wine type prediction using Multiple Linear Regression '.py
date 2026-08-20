
import numpy as np 
import pandas as pd 
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


# Import Dataset 

columns=[
    "Alchol_Type",
    "Malic acid",
    "Ash",
    "Alcalinity of ash",
    "Magnesium",
    "Total Phenol",
    "Flavanoids",
    "Nonflavanoid phenols",
    "Proanthocyanins",
    "Color intensity",
    "Hue",
    "OD280/OD315 of diluted wines",
    "Proline ",

]

dataset=pd.read_csv(r"C:\Python learning\Python Projects\#4 Model For predicting Alchol class\Wine dataset\wine.csv",names=columns)


print(dataset.head(10))

X=dataset[[  "Malic acid",
    "Ash",
    "Alcalinity of ash",
    "Magnesium",
    "Total Phenol",
    "Flavanoids",
    "Nonflavanoid phenols",
    "Proanthocyanins",
    "Color intensity",
    "Hue",
    "OD280/OD315 of diluted wines",
    "Proline ",]]

Y=dataset["Alchol_Type"]



# Split the training & Testing data 


X_Train,X_Test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,random_state=42)


# Train model 

model=linear_model.LinearRegression()



model.fit(X_Train,Y_train)


predict_y=model.predict(X_Test)


print("Mean squared error  : ",mean_squared_error(Y_test,predict_y))



