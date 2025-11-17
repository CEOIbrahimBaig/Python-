def greates_val (a,b,c):
    if (a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b 
    else :
        return c

a= int(input("Please enter the value of a "))
b= int(input("Please enter the value of b "))
c= int(input("Please enter the value of c "))



print ("The greatest value is ",greates_val(a,b,c))
      
    