
                      # Logistic Regression 
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt 

#Load Dataset 
iris=datasets.load_iris()


X=iris["data"][:,3:] # Selected  only one  column 

print(X)

Y=(iris["target"]==2).astype(np.int_) # Selected rows only for Iris Variginica

print(Y)


# Training logistic regression calssifier 

model=LogisticRegression()

model.fit(X,Y)



# Doing prediction 

prediction=model.predict(([[2.7]]))

print (prediction)



# Using matplotlib to plot visualisation 

Petal_width_of_different_plants =np.linspace(0,3,1000).reshape(-1,1)
# CREATED A 1D ARRAY OF DIFFERENT  PETAL LENGTHS 

probability_to_be_iris_vargina=model.predict_proba(Petal_width_of_different_plants)

plt.plot(Petal_width_of_different_plants,probability_to_be_iris_vargina)

plt.xlabel("Verginica ")

plt.show()