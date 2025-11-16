# Task to find factorial of a number 

number=int(input("\tPlease enter the Number whoose factorial you want \n"))

factorial=1

if (number==0 or number==1 ):
    print ("The  factorial of given number is ",factorial)
else :
    for i in range(1,number+1): # Used number +1 because range (start,end-1 )
    # it end before number so need to add +1 in number 
     factorial=factorial*i
    

print ("The factorial of ",number," is ",factorial)