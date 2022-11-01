
import math
from re import L
  
# A function to print all prime factors of 
# a given number n
def primeFactors(n):
      
    # Print the number of two\'s that divide n
    while n % 2 == 0:
        print 2,
        n = n / 2
          
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
          
        # while i divides n , print i ad divide n
        while n % i== 0:
            print i,
            n = n / i
              
    # Condition if n is a prime
    # number greater than 2

          
# Driver Program to test above function
  

	
list = []


def mmm(number_one,number_two):
    global list
    one_factors = primeFactors(number_one)
    ffone = number_one[1]
    sfone = number_one[3]
    tfone = number_one[5]
    fofone = number_two[7]
    two_factors = primeFactors(number_two)
    ffsecond = number_two[1]
    sfsecond = number_two[3]
    tfsecond = number_two[5]
    fofsecond = number_two[7]
    if ffone == ffsecond or ffone == sfsecond or ffone == tfsecond or sfone == fofsecond:
        list.append(ffone)
    if sfone == tfsecond or ffone == sfsecond or ffone == tfsecond or sfone == fofsecond:
        list.append(sfone)
    if tfone == tfsecond or ffone == sfsecond or ffone == tfsecond or sfone == fofsecond:
        list.append(tfone)
    if fofone == fofsecond or ffone == sfsecond or ffone == tfsecond or sfone == fofsecond:
        list.append(fofone)
    else:
        list.append(0)
    
    thenumberyouwant = list[1]*list[2]*list[3]*list[4]