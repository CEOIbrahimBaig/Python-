
                      # Introduction 


'''
The name Pandas come from Panel Data .

Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" 
and was created by Wes McKinney in 2008.



'''




               # Why Use PANDAS  

'''

Pandas gives you answers about the data. Like:

Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?
Pandas are also able to delete rows that are not relevant, 
or contains wrong values, like empty or NULL values. This is called cleaning the data.


'''
import pandas as pd

data={

"column1":[6,7,3],
"column2":[2,3,5]


}

abj = pd.DataFrame(data)

print (abj)




