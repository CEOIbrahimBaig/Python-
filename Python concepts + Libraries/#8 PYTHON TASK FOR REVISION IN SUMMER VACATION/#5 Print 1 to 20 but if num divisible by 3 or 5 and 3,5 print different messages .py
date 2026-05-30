
a=3
b=5

for i in range(1,20):

    if i%b==0 and i%3==0 :
        print("FIZZBUZZ")

    elif i%a==0 : 
        print ("FIZZ")
    elif i%b==0 :
        print  ("BUZZ")
   
    else:
        print(i)
    
