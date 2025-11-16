
# Multiplication table 

table=int(input("\tPlease enter the number whoose multiplication table you want \n"))

print ("\t Multiplication table for ",table)


for i in range(0,10):
    print(table," * ",i," = ",table*i)
    i+=1
