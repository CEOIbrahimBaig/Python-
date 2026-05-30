# Per subject pass requirement = 40% 
# Total marks pass requirement = 33 % 
# 3 Students and 3 Subject 
# Marks for each subject will be entered by the user 

marks_in_math ={
"Hafsa":0,
"Ibrahim":0,
"Ali":0,
}

marks_in_coding={
"Hafsa":0,
"Ibrahim":0,
"Ali":0,
}
marks_in_cpp ={
"Hafsa":0,
"Ibrahim":0,
"Ali":0,
}

student1_math=int (input("\tHafsa , Please Enter your marks in math \n"))
student1_coding=int (input("\tHafsa , Please Enter your marks in coding \n"))
student1_cpp=int (input("\tHafsa , Please Enter your marks in cpp \n"))

student2_math=int (input("\tIbrahim , Please Enter your marks in math \n"))
student2_coding=int (input("\tIbrahim , Please Enter your marks in coding \n"))
student2_cpp=int (input("\tIbrahim , Please Enter your marks in cpp \n"))


student3_math=int (input("\tAli , Please Enter your marks in math \n"))
student3_coding=int (input("\tAli , Please Enter your marks in coding \n"))
student3_cpp=int (input("\tAli , Please Enter your marks in cpp \n"))

marks_in_math.update({"Hafsa":student1_math,"Ibrahim":student2_math,"Ali":student3_math})
marks_in_coding.update({"Hafsa":student1_coding,"Ibrahim":student2_coding,"Ali":student3_coding})
marks_in_cpp.update({"Hafsa":student1_cpp,"Ibrahim":student2_cpp,"Ali":student3_cpp})


hafsa_marks=[marks_in_math["Hafsa"],marks_in_coding["Hafsa"],marks_in_cpp["Hafsa"]]
Ali_marks=[marks_in_math["Ali"],marks_in_coding["Ali"],marks_in_cpp["Ali"]]
Ibrahim_marks=[marks_in_math["Ibrahim"],marks_in_coding["Ibrahim"],marks_in_cpp["Ibrahim"]]

sumofhafsa=sum(hafsa_marks)
sumofibrahim=sum(Ibrahim_marks)
sumofali=sum(Ali_marks)


if(sumofhafsa/3>33):
    print("Hafsa passed the exam , Congrats SHE IS PROMOTED ")

else:
    print("Hafsa failed the exam")


if(sumofibrahim/3>33):
    print("Ibrahim passed the exam , Congrats HE IS PROMOTED ")

else:
    print("Ibrahim  failed the exam")


if(sumofali/3>33):
    print("Ali  passed the exam , Congrats HE IS PROMOTED ")

else:
    print("Ali failed the exam")



