#print the following using loops 
# ***
# * *
# ***

n=3 

for i in range (0,n):
  if (i==1):
    print("* *")
  else:
    print ("***")

print ("Using Non hard coded method ")
n = int(input("Please enter the length of square "))

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
