"""


Create a function that finds how many prime numbers there are, up to the given
integer.

### Examples

    prime_numbers(10) ➞ 4
    # 2, 3, 5 and 7
    
    prime_numbers(20) ➞ 8
    # 2, 3, 5, 7, 11, 13, 17 and 19
    
    prime_numbers(30) ➞ 10
    # 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

### Notes

N/A

"""

from functools import reduce
​
def prime_numbers(num):
  numOfPrime = 0
  for a in range (1, num + 1):
    if factors(a):
      numOfPrime += 1
  return numOfPrime
      
​
def factors(n):
  return len(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))) == 2

