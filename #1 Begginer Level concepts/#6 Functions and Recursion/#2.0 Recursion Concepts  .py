 
# Recursion is a proccess in which a function call itself 

# The require a base condition , if there is no base condition in a function 
# It cant be made as a recursion function 


def factorial (n ):
    if (n==0 or n==1 ): # This line of code is a base condition 
        return 1 # Thie line of code is returning a base value 
    else:
        return n*factorial(n-1) # This line of code is returning a recursive condition 
    
    
    

n = int (input("Please enter a number whose factorial you want "))

print (factorial(n))


