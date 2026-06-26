

                                       # Wrong Data Handling 



'''

"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong,
 like if someone registered "199" instead of "1.99".

Sometimes you can spot wrong data by looking at the data set, because you have an expectation 
of what it should be.

'''



#Replacing Values 




import pandas as pd 

abj=pd.read_csv(r"C:\Python learning\Python concepts + Libraries\#11 Pandas Library\Cleaning data with Panda\Dataset.csv")


abj.loc[0,"Duration"]=99

print (abj.to_string())



# If ANY DURATION IS > 120 MAKE  IT 120 

for x in abj:
    if abj.loc[x,"Duration"]>120:
        abj.loc[x,"Duration"]=120



# If ANY DURATION IS > 120 REMOVE THE ROW 

for x in abj:
    if abj.loc[x,"Duration"]>120:
        abj.dropna(x,inplace=True)


