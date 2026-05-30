def temp (temp_celcius):
    return temp_celcius*(9/5)+32
  
temp_celcius= int(input("Please enter the value of temp in celcius "))

print ("The temp in Farenhite is ",temp(temp_celcius))