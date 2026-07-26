
                      # Multiple Linear Regression 
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Loading database 

iris=datasets.load_iris()


# CREATING INPUT & OUTPUT  

features=iris.data
labels=iris.target

# print(features[0],labels[0])


#Selecting model type 

classifier=KNeighborsClassifier()

# Training model 

classifier.fit(features,labels)


# Predicting through Model 

prediction =classifier.predict([5.1,3,2,1])

print (prediction)