



                                    # Pandas - Analyzing DataFrames

'''
Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in 
the world of programming, including Pandas.

In our examples we will be using a JSON file called 'data.json'.



'''

import pandas as pd 

   
abj=pd.read_csv(r"C:\Python learning\Python concepts + Libraries\#11 Pandas Library\Basics of Panda\Panda_read_it.csv")


print(abj.head(10))


print ("\n",abj.head()) # It will print First 5 Rows Of data 

print ("\n",abj.tail(10))

print ("\n",abj.tail()) # It will print Last 5 Rows Of data 




print (abj.info())



''''

The info() method also tells us how many Non-Null values there are present in each column, 
and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever 
reason.

Empty values, or Null values, can be bad when analyzing data, and you should consider removing 
rows with empty values. This is a step towards what is called cleaning data


'''


