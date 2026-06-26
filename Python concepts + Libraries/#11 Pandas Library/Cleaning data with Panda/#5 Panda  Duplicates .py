

                                       # Duplicates 



'''


'''



#Replacing Values 




import pandas as pd 

abj=pd.read_csv(r"C:\Python learning\Python concepts + Libraries\#11 Pandas Library\Cleaning data with Panda\Dataset.csv")


# To find Duplicate rows use 


print(abj.duplicated().to_string())


# To Remove Duplicates Use 

abj=abj.drop_duplicates()

