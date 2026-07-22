
                      # Introduction 

import numpy as np 
import matplotlib.pyplot as plt 

from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

# Loading diabaties dataset from sklearn 

diabetes=datasets.load_diabetes()


print(diabetes.keys())


diabetes_x=diabetes.data[:,np.newaxis,2] #[rows,columns]  The axis function increase dimension of Array

print(diabetes_x)


diabetes_x_train=diabetes_x[:-30] # Input for training 

diabetes_x_test=diabetes_x[-30:] # Input for testing 



diabetes_y_train=diabetes.target[:-30]  # Output for training
diabetes_y_test=diabetes.target[-30:]   # Output for testing 

model=linear_model.LinearRegression()


model.fit(diabetes_x_train,diabetes_y_train)

diabetes_y_predict=model.predict(diabetes_x_test)



print ("Mean squared error : ",mean_squared_error(diabetes_y_test,diabetes_y_predict))

print ("Wegiths  : ",model.coef_)
print ("Intercept : ",model.intercept_)


plt.scatter(diabetes_x_test,diabetes_y_test)

plt.show()
plt.plot(diabetes_x_test,diabetes_y_predict)

plt.show()