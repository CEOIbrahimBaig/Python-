 

                           # Extracting data from CSV Files using Pandas 




import pandas as pd 


data=pd.read_csv(r"C:\Python learning\Python Projects\#3 Gym progress & Fitness Analytics\Gym_dataset.csv")



data_required=data["Calories"] # Give whole column of calories 

print  (data_required)

whole_row=data.loc[0]  # Gives a whole  row 


print (whole_row)

whole_row=data.loc["1/1/2026"]

print (whole_row)


specific_cell=data[2,"Calories"]



# learnt the  row ,column concepts . loc and min max mean median mode ok for next day 

max_calories=data["Calories"].max() # Fro max value in a column .

min_calories=data["Calories"].min() # For Min value in a column .

Average_calories=data["Calories"].mean() # For average of all the column 

most_repeated_calories_consumption=data["Calories"].mode() # To get the most repeated value from the column 

mid_calories_value=data["Calories"].median() # It sort all values and give value that come at mid 


