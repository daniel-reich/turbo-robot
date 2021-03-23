"""


Create a function that takes a list of numbers and returns the **sum** of all
**prime numbers** in the list.

### Examples

    sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
    
    sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
    
    sum_primes([]) ➞ None

### Notes

  * Given numbers won't exceed 101.
  * A prime number is a number which has exactly two divisors.

"""

def sum_primes(lst):
  def check_prime(num):
    is_prime = True
    for i in range(2,num-1):
      if (num%i) == 0:
        is_prime = False
        break
    return is_prime  
  sum_primes = 0
  if lst == []:
    return None
  for num in lst:
    print ("The number is " , num , "and the prime is " , check_prime(num)) , " ."
    if num > 1 and check_prime(num) == True:
      sum_primes += num
​
  return sum_primes

