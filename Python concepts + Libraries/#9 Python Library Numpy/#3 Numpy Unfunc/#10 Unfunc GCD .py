
                              # Numpy  GCD

'''The GCD (Greatest Common Divisor), also known as HCF
 (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.
'''

import numpy as np

n1=6
n2=9



x=np.gcd(n1,n2)

print(x)


arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)


