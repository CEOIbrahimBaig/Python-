
                      # Multiple Linear Regression 

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


# Loading diabaties dataset 


columns=[
"Sepal_length",
"Sepal_width",
"Petal_length",
"Petal_width",
"Name"
] # Because dataset has no heading for columns

dataset=pd.read_csv(r"C:\Python learning\Python concepts + Libraries\#12 Sickit Learn Library\Iris Dataset\iris.csv",names=columns)


print(dataset.head())


# Seprate Input features = X & Output  = Y
X=dataset[["Sepal_length",
"Sepal_width",
"Petal_length",

]]

Y=dataset["Petal_width"]

# Splitting data for test & Training using function 


X_train,X_Test,Y_train,Y_Test=train_test_split(X,Y,test_size=0.2,random_state=42)




# Train model 

model=linear_model.LinearRegression()


model.fit(X_train,Y_train)

# Prediction & Mean square error 

predict_y=model.predict(X_Test)


print("Mean squared error  : ",mean_squared_error(Y_Test,predict_y))



