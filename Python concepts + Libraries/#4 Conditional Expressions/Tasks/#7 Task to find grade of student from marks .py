marks=int(input("\t Please enter your marks \n "))

if (marks<=0):
    print("Ustad kay sath panga hai koi jo itnay ziada numbers mil gay apko \n")

elif(marks>0 and marks<50):
    print("You got an F ")
elif(marks>=50 and marks<60 ):
    print ("You got D")
elif(marks>=60 and marks<70):
    print("You got a C")
elif (marks>=70 and marks<80 ):
    print("You got a B")
elif (marks>=80 and marks<90):
    print("You got an A")
else :
    print("You got an Ex")
    