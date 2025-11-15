# Task to  find if the given number by user is prime or not 

number= int (input("\t Please enter the number which you want to check \n"))


if number <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, number):  # just check all numbers from 2 to number-1
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")
