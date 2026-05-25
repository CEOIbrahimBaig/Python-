

languages=["CPP","Java","Lua",'C#','PHP']

languages[2]='Python'
print (languages)


#2 Task 2 is to do the same with tuple 

''' As tuple is immutable so we will do this 

-> make tuple = list 
-> change data 
-> make list = tuple 
'''


lan=("CPP","Java","Lua",'C#','PHP')

temporary = list(lan)

temporary[2]= 'PYTHON'

lan= tuple(temporary)

print (lan )