#print the following using loops 
# *
# **
# ***

print ("By using only single loop ")
for i in range (1,4):
    print ("*"*i,end="")
    print("")

   
print ("By using only Nested loop ")
for i in range (0,3):
    for j in range(0,i+1):
        print("*",end="")
    print()
  

print ("Now printing by using while loop ")

i= 0



while(i<3):
    j=0
    while(j<i+1):
        
        print("*",end="")
        j+=1
    i+=1
    print()