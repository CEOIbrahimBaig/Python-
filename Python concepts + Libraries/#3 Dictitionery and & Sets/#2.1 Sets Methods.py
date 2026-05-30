s={1,2,4,5,6,7,"Harry "}


# Properties of set 

# It is unorderd 
# Can't Access element by the index 
# It is not  mutable 
# Can't have duplicate values 



# 1st Method .add() It adds a new data at the end , Repetitive data is not added 

s.add(78)

print(s)


# 2nd Method .lent(set) Pint the length of set 

print(len(s))

#3rd Method .remove(value)  To remove a certain  value from the set 

s.remove ("Harry ") 

print (s)

#4th Method  .pop() To remove a random element from the set 
# An arbitary element is removed from the set  (Pseudo-random)

s.pop()

print(s)

#5th  Method .clear Empty the Set 

s.clear() # The whole set is now empty 

print (s )

#6th Taking union of two sets 


a1={1,2,5,6}
a2={7,4,2,1}

print(a1.union(a2))

#7TH Method Intersection of two sets 

print(a1.intersection(a2))

