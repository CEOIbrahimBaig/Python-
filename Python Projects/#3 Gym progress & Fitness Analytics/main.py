
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# Phase #1 Data Loading & Exploration 


# Checking if data loaded corretly 
'''print(data.head(5)) 
print (data.info())

'''
# Checking the datatypes of data 

''' print (data.dtypes) '''



# Starting the Project 

print ("\tDear User, \nWhat would You like to view ")

input_by_user=input(" Dashboard =1 \n Max & Minimum Calories consumed = 2 \n Average Calorie intake = 3 \n Average protein intake =4 \n Personal Record = 5  ")


   # For max and min Calories  

if input_by_user=="2":
    max_calories=0
    for x in data.index:
        if data.loc[x,"Calories"]>max_calories:
             max_calories=data.loc[x,"Calories"]

    # We will use easy way for min which could also be used for the above one 
    min_calories=data["Calories"].min()

    print ("Max Calories :",max_calories,"\n Minimum Calories :",min_calories)


 # For Average_calorie_intake 

if input_by_user=="3":
    Average_calories=data["Calories"].mean()

    print ("Average Calories : ",Average_calories)



if input_by_user=="4":
    Average_protein=data["Protein"].mean()

    print ("Average Protein Intake : ",Average_protein)


if input_by_user=="5":

    max_bench_press=data["Bench_Press"].max()
    max_squat=data["Squat"].max()

    print("You Personal Highest Recording are following ")
    print ("Max Bench Press  :",max_bench_press ," Date : ",data.loc["Date"].where(data.loc["Bench_Press"].max()))
    print ("Max Squat : ",max_squat," Date : ",data.loc["Date"].where(data.loc["Squat"].max()))


if input_by_user=="5":

    daily_calories=data["Calories"].values
    bench_press=data["Bench_Press"].values
    dates=data["Dates"].values
    


  #  plt.subplot(2,2,2)
  #  plt.scatter()