
def sum_of_n(n):
    if (n<=0 ):
        return 0 
    else:
        return sum_of_n(n-1)+n


n =int  (input ("\tPlease enter the Number whoose Sum you want \n"))

print ("The Arithmatic sum of  given neutral number is ",sum_of_n(n))
