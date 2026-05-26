s={}

name1=input("\tPlease enter your name\n ")
f1=input("\tPlease enter your Favourite Language \n")

name2=input("\tPlease enter your name\n ")
f2=input("\tPlease enter your Favourite Language \n")

name3=input("\tPlease enter your name\n ")
f3=input("\tPlease enter your Favourite Language \n")

name4=input("\tPlease enter your name\n ")
f4=input("\tPlease enter your Favourite Language \n")

s.update({name1:f1})
s.update({name2:f2})
s.update({name3:f3})
s.update({name4:f4})
print (s)



# Bugs  I caused 
#1 I used add instead of update 
#2 I Forgot to use {} and I mistookly used () only , the correct version is ({key:vakue})
#3 I Forgot to use : in ({key:values}) , I instead wrote ({key,values})