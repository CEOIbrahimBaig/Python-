

                                       # Wrong Format  



'''
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

To fix it, you have two options: remove the rows, or 
convert all cells in the columns into the same format.'''




#1st method = Convert the data into correct form date 


import pandas as pd 

abj=pd.read_csv(r"C:\Python learning\Python concepts + Libraries\#11 Pandas Library\Cleaning data with Panda\Wrong_format_dataset.csv")


abj["Date"]=pd.to_datetime(abj["Date"],format="mixed")



# Either you can remove all the null values 

abj=abj.dropna(inplace=True) # It will drop all the rows with null values 


# Or You can drop the rows only having date as null 

abj=abj.dropna(subset=["Date"])



