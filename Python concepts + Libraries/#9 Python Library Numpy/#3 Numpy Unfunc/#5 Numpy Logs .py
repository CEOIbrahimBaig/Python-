
                              # Numpy Logs 


#   What is log 

'''

In simple terms, a logarithm (or log) is the opposite of an exponent. 

It answers the question:"How many of this number do I need to multiply together 
to get that number?


"Think of it as a "counting multiplications" machine.

### A Simple Example
We all know how exponents work:
2³ = 2 × 2 × 2 = 8
*(Here, we start with 2, multiply it 3 times, and get 8.)*

A logarithm just flips that question backward:
log₂(8) = 3

*(This reads as: "What is the log, base 2, of 8?" It’s asking: "
How many 2s do I have to multiply together to get 8?" The answer is 3.)*

'''

# Here 2 is Base 
# Here 8 is Target or Argument 
# Here 3 is Exponent 


                               # Log Base 2 


import numpy as np 

arr=np.arange(1,10)  # It creates  a Numpy array starting from 1 till 10 


print(np.log2(arr))

                             # Log Base 10 

print("\n",np.log10(arr))

                            # Natural Log or Log base e 

print("\n",np.log(arr))



                            # Log  at any base 

from math import log 


any_base_log_func=np.frompyfunc(log,2,1)

print("The log for array at base 10 and target 15 is ",any_base_log_func(15,10))#func(target,base)



