 

                           # Extracting data from CSV Files using Pandas 




import pandas as pd 


data=pd.read_csv(r"C:\Python learning\Python Projects\#3 Gym progress & Fitness Analytics\Gym_dataset.csv")



data_required=data["Calories"] # Give whole column of calories 

print  (data_required)

whole_row=data.loc[0]  # Gives a whole  row 


print (whole_row)

whole_row=data.loc["1/1/2026"]

print (whole_row)



# learnt the  row ,column concepts . loc and min max mean median mode ok for nex day 