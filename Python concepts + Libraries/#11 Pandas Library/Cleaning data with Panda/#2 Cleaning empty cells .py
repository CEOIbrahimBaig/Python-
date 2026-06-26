

                              # Cleaning Empty cells 



#1st Method Remove whole row 

''' It is better only if the dataset is large and everything is not important '''


import pandas as pd 

abj=pd.read_csv(r"C:\Python learning\Python concepts + Libraries\#11 Pandas Library\Cleaning data with Panda\Dataset.csv")

new_abj=abj.dropna() # It will not change orignal data , It will create new one with empty cells removed


print (new_abj.to_string())


# In order to create effect on the real data use following method 

abj.dropna(inplace=True) # it will remove null values from variable strong dataset 

# Instaead of it you can just write 
abj=abj.dropna()




                           # Replace Empty Values 


abj.fillna(30 ,inplace=True)   # Fill 30 in empty cells 
# Either you can use above ay to fill empty cells or below one 


abj=abj.fillna(30)

print (abj.to_string())


# If YOU WANT TO FILL SPECIFIC Column

abj=abj.fillna({"Calories":30},inplace=True)




# Another Method to replace Empty  cells is by  Mean , Median and Mode 


x=abj["Calories"].mean()

abj=abj.fillna({"Calories":x})


# Mean = Average , 

# Median = Mid 
x=abj["Calories"].mode()

abj=abj.fillna({"Calories":x})


# Mode =Most occured Value 


a=abj["Calories"].mode()[0]

abj.fillna({"Calories":a},inplace=True)





