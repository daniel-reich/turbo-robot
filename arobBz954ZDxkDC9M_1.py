"""


Given an integer, create a function that returns the next prime. If the number
is prime, return the number itself.

### Examples

    next_prime(12) ➞ 13
    
    next_prime(24) ➞ 29
    
    next_prime(11) ➞ 11
    # 11 is a prime, so we return the number itself.

### Notes

N/A

"""

##Alrighty, this is ugly, but it passes the tests, so let me explain.
​
​
def next_prime(num):
  first_checker = []           #Checks if first number is prime
  last_checker = []            #Checks if each subsequent number is prime
  prime_checker = False        #Assigning Boolean to a prime_checker var
  new_num = num + 1            #I don't need this, but it made things handy
  for i in range(2, num):
    if num % i == 0:           #Standard boolean checker, except wanted to see if I could implement array. After loop, if len(array) == 2, number is prime as is.
      continue
    else:
      first_checker.append(i)
  if len(first_checker) > 2:   #Checking if initial number is non-prime
    while prime_checker == False: 
      for i in range(2, new_num): #checking next number
        if num % i == 0:
          continue
        else:
          last_checker.append(i)  #Same concept. If post loop, len(last_checker) == 2, num is prime
      if len(last_checker) == 2:  #See above
        prime_checker = True      #Stop while loop
        return i                  #Return prime number
      else:
        new_num += 1              #If not prime, increment to next number, try again

