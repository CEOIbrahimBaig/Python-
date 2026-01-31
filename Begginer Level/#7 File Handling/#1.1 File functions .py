

'''

#f =open("C:/Python learning/Begginer Level/#7 File Handling/file.txt")
# OPEN () First parmeter is for path , 2nd is for mode 
# The deafault 2nd paramter is "r" for reading 

#1st Method  .readlines() Returns the line in string form 

f=open("C:/Python learning/Begginer Level/#7 File Handling/file.txt")

data=f.readline()
data2 =f.readline () # Will display the next line 


print (data)
print(data2)


#3rd Method .readlines() print the lines in list form 

# It will be empty because .readline() function move pointer forward 
# It will start printing data from 3rd line to onwards 

lines =f.readlines()

print (lines)

# If you use readline even with no data , then you get empty string 


'''

#For iteration with while loop 

#f=open("C:/Python learning/Begginer Level/#7 File Handling/file.txt")

'''    lines =f.readline()
    while (lines!=""):
        print (lines)
        line=f.readline()
'''

f = open("C:/Python learning/Begginer Level/#7 File Handling/file.txt")

lines = f.readline()   # read the first line
while lines != "":     # loop until empty string
    print(lines)
    line = f.readline()  # read next line and update the same variable

f.close()
