
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
# Phase #1 Data Loading & Exploration 

data=pd.read_csv(r"C:\Python learning\Python Projects\#3 Gym progress & Fitness Analytics\Gym_dataset.csv")

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


if input_by_user == "5":
    # 1. Grab the highest numeric values from the columns
    max_bench_press = data["Bench_Press"].max()
    max_squat = data["Squat"].max()

    # 2. Use .idxmax() to find the precise row index number where that max value sits
    bench_index = data["Bench_Press"].idxmax()
    squat_index = data["Squat"].idxmax()

    # 3. Pull the actual date string from that exact row index position
    bench_pr_date = data.loc[bench_index, "Date"]
    squat_pr_date = data.loc[squat_index, "Date"]

    print("Your Personal Highest Recordings are following:")
    print("Max Bench Press :", max_bench_press, "kg | Date :", bench_pr_date)
    print("Max Squat       :", max_squat, "kg | Date :", squat_pr_date)

    
if input_by_user=="1":

    daily_calories=data["Calories"].values
    bench_press=data["Bench_Press"].values
    dates=data["Date"].values
    squats=data["Squat"].values

    plt.subplot(2,2,1)
    plt.scatter(daily_calories,bench_press,marker='o',color="hotpink") # For daily calories versus banch press
    plt.xlabel("Calories")
    plt.ylabel("Weight of bench press") 
    plt.title("Calories versus Weight")

    plt.subplot(2,2,2)
    plt.hist(daily_calories,bins=12)
    

    plt.subplot(2,2,3)
    plt.plot(dates,bench_press,dates,squats,"o:g")
    plt.plot(dates,bench_press,dates,squats,"s-b")
    plt.xlabel("Time")
    plt.ylabel("Wights")
    plt.title("Comparison of Weights over time ")
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(14))

    plt.show()

    