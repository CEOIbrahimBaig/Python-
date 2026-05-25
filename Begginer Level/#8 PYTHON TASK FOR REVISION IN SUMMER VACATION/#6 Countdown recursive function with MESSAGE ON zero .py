def countdown(n):
    
    if n==0 :
        print("BOOM Blastoff")
        return n
    else :
     print(n)
     return countdown(n-1)
    


    

a=int(input("Please enter the time for countdown "))

countdown(a)

