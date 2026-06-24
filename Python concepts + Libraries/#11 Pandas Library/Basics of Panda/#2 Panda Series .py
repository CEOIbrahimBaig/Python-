 

                                 # Panda Series  


''' 

   A series is Like a column in a table  . 

   It is one Dimensional Array holding data of any type .


'''


import pandas as pd 


a=[5,3,2]

values=pd.Series(a)

print (values)


# Normally the indexes are marked from 0,1,2,3 ....... But you can create manual names also 


b=["Harry","Ali","Ahmed","Hafsa","Ibrahim"]

ab=pd.Series(b,index=["1st _student","2nd Student","Third Student","4th Student","5th Student"])

print(ab)


#  Theese are also called as labels , You can use these labels same as indexes are used 


print ("\n",ab["2nd Student"])



# Series can also be created by using dictionary 


calories_count={
    "Day 1 ":2220,
    "Day 2":2460,
    "Day 3":2900
}

am=pd.Series(calories_count)
print("\n",am )

# You can also create  a variable containing specific indexes

am=pd.Series(calories_count,index=["Day 1","Day 2"])

print(am)



                                  #DataFrames

'''Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

Series is like a column, a DataFrame is the whole table.
'''


data={
    
"Calories":[1222,4244,2020],
"Duration":[20,60,220]

}

abj=pd.DataFrame(data)
print( "\n",abj)


