                                    #  Ecommerce Sales Tracking 



import numpy as np 
import matplotlib.pyplot as plt 
# There are 3  Products and 7 days so shape of array is (3,7)

arr=np.array([
    [10,14,22],   # Monday sales
    [22,355,66],   # Tuesday sales 
    [44,42,1],   # Wednesday sales 
    [33,11,9],   # Thursday sales 
    [585,1,2],   # Friday sales 
    [9,22,11],   # Saturday sales 
    [382,33,1]    # Sunday sales 
])
weeks=np.array(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])


weekends=int(input("Do You want to know sales of Weekends \n For Weekend Type 1 \n For Specific day Type 2\n"))

if weekends==1: 
   print("The sales of Caps ,Bages and Shoes on weekends are \t ",arr[5:])
   plt.plot(arr[5:,0],label="Caps",) # for caps a line =Blue 
   plt.plot(arr[5:,1],label="Bags") # For bags a line = Orange 
   plt.plot(arr[5:,2],color='hotpink',label="Shoes") # For Shoes a line = hotpink
   plt.show()



if weekends==2 :
    day=input("Enter the Name of day of which you want to extract sales detail ")
    Product= input ("Enter  the Product or Products You want to get sales detail\nFor Caps Type 1 \n For Bags Type 2 \n For Shoes Type 3 ")
    
    if day=="Monday": 
     row=0 
    elif day=="Tuesday":
      row=1
    elif day=="Wednesday":
     row=2
    elif day=="Thursday":
     row=3
    elif day=="Friday":
     row=4
    elif day=="Saturday":
     row=5
    elif day=="Sunday":
     row=6
    else  :
     print ("Please enter the correct date \n")
     
    if Product=="1" : 
       column=0
    elif Product=="2":
      column=1
    elif Product=="3":
      column =2

    print("The sales are ",arr[row,column])
    plt.plot()





    
    
