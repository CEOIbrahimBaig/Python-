''' The template is 
Dear USERNAME 
                 You are selected
                 Date_user_given 

Print same Template by using the user data 
'''
'''name=input("Please Enter your Name \n")
date=input("Please Enter your Date for Request Submission \n")

print ("\tDear ",name)
print ("\tYou are Selected\n")
print("Date = ",date)
'''

template=''' The template is 
Dear USERNAME 
                 You are selected
                 Date_user_given 

Print same Template by using the user data 
'''

template=template.replace("USERNAME","Ibrahim").replace("Date_user_given","20-10-2025")

print(template)