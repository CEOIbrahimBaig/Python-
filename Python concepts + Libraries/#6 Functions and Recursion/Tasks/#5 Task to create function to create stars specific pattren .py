# ***
# **
# *


        
def print_pattern(rows):
    if rows <= 0:
        return "Give a valid number of rows please"

    abj = ""   # start empty string

    for i in range(rows):
        abj += "*" * (rows - i) + "\n"   

    return abj   # return full pattern at the END



rows= int (input("Please enter the number of rows you want "))

print (print_pattern(rows))




'''
def print_pattren (rows ):
   if (rows<0):
      return  "Give a valid number of rows please "
   elif (rows>0):
      for i in range(0,rows):
         abj="*"*rows-i+"\n"
         i+=1
    return abj
    
        
'''