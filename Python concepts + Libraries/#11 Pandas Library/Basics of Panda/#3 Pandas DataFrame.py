


                                  # Pandas DataFrame 

'''
A dataframe is  a two dimensional structure like 2 Dimensional Arrays with rows and columns 


'''

import pandas as pd


data={

"Calories":[122,444,666],
"Duration":[20,30,10]

}

dataset=pd.DataFrame(data,index=["Day 1","Day 2","Day 3"])

print(dataset)


# You can print specific  row by mentioaning a name of the index

print ('\n',dataset.loc["Day 3"])


