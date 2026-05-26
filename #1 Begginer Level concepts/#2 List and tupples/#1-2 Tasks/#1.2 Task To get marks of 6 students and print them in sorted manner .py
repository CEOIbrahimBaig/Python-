marks= []

s1 = int(input("\t Please enter 1st student marks \n"))

marks.insert(0,s1)

s2 = int(input("\t Please enter 2nd student marks \n"))

marks.insert(1,s2)

s3 = int(input("\t Please enter 3rd student marks \n"))

marks.insert(2,s3)

s4 = int(input("\t Please enter 4th student marks \n"))

marks.insert(3,s4)

s5 = int(input("\t Please enter 5th student marks \n"))

marks.insert(4,s5)


s6 = int(input("\t Please enter 6th student marks \n"))

marks.insert(5,s6)

print ("\tMarks before  sorting \n \t",marks)


marks.sort()
print ("\t Marks after sorting \n \t ",marks)

