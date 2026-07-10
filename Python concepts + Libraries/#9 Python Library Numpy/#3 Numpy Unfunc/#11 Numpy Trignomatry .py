
                              # Numpy  Trigonometric Unfunc

'''
NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and 
produce the corresponding sin, cos and tan values.

'''
import numpy as np


x=np.sin(np.pi/2)


print (x)



arr =np.array([np.pi,np.pi/2])


print(np.cos(arr))


arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)



arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)


                                   # Finding Angles 



x= np.arcsin(1.0)


print (x)



arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)






                                   # Hypotenus 


base=2
prependicular=3


result=np.hypot(base,prependicular)

print ("\n",result)

