


                                  # Pandas Read CSV file 


import pandas as pd

do=pd.read_csv(r"C:\Users\User\Desktop\Panda_read_it.csv")

print(do.to_string()) # Print in the form of Series 


ab = pd.read_csv(r"C:\Users\User\Desktop\Panda_read_it.csv")

print (ab) # It will print in form DataFrame

print (pd.options.display.max_rows)


# To change then Numbers of rows that will be displayed by the DataFrame change the max rows value 

pd.options.display.max_rows=999

print (ab)
