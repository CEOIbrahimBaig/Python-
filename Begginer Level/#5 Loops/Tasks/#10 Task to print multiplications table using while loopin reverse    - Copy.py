# Multiplication table 

table=int(input  ("\tPlease enter the Number whoose multiplication table you want \n"))

i=0;

print("\tThe Multiplication table for ",table,"is shown below\n")

while  (i<11):
    print (table," * ",table-i," = ",table*(table-i))
    i+=1


