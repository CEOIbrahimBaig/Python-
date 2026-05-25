# Write a program to great a user with good day 

def greet (name):
 #  The "() are  called as parenthesis  and data in it is an Argument 
    print ("Hi ",name)


# You can also addd multiple arguments in one function  
def greet_end (name,ending):
 #  The "() are  called as parenthesis  and data in it is an Argument 
    print ("Hi ",name)
    print (ending )


greet_end("Ali","Bye ") 



# A function can also return a value 

def sum(a,b):
    
    return a+b

c=int(input("Please enter the value you want  to add "))
d=int(input("Enter the 2nd value you want to add in first one "))
val=sum(c,d)

print (val)