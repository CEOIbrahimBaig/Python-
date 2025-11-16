# Task to  find if the given number by user is prime or not 

n= int (input("\t Please enter the number which you want to check \n"))

for i in range (2,n):
    if ((n%i)==0):
        print ("Number is not prime ")
        break
    
else :
    print ("Number is prime ")