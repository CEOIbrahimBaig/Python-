                                            # DICTIONERIES 

# Used to store related  data togather 

#It is unorderd ,for  searching  it dont see  all related data type , take big oh  1 to  print 
#It is mutable 
#It is indexed 
#Can not contain duplicate keys 


c="Ali_hassan"


marks = {
    "Ibrahim":100,
    43:'HAFSA',
    c:70,
    0:"Harry"
}
# Same can be done by list but problem is it would prints slow and can't print using mapped data
# Before colon key is present which is used to show the mapped value 

print (marks,type(marks)) # Print data and data type 

print (marks[43])

print (marks)