
                              # Numpy LCM


import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)

# Returns: 12 because that is the lowest common multiple of both numbers (4*3=12 and 6*2=12).


arr=np.array([3,6,9])


print(np.lcm.reduce(arr))



arr=np.arange(1,10)

print(np.lcm.reduce(arr))

