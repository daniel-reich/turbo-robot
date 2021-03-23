"""


The Kempner Function, applied to a composite number, permits to find the
smallest integer greater than zero whose factorial is exactly divided by the
number.

    kempner(6) ➞ 3
    
    1! = 1 % 6 > 0
    2! = 2 % 6 > 0
    3! = 6 % 6 === 0
    
    kempner(10) ➞ 5
    
    1! = 1 % 10 > 0
    2! = 2 % 10 > 0
    3! = 6 % 10 > 0
    4! = 24 % 10 > 0
    5! = 120 % 10 === 0

A Kempner Function applied to a prime will always return the prime itself.

    kempner(2) ➞ 2
    kempner(5) ➞ 5

Given an integer `n`, implement a Kempner Function.

### Examples

    kempner(6) ➞ 3
    
    kempner(10) ➞ 5
    
    kempner(2) ➞ 2

### Notes

  * Try solving this recursively, with an approach oriented to higher-order functions.
  * If you need to get more confident with recursion and factorials, try [this challenge](https://edabit.com/challenge/wRf3e8T3vQpG7SmjP).

"""

import math
def kempner(n):
  #find lowest integer which factorial divides into n 
  if isItPrime(n):
    return n
  else:
    for x in range(1,n+1):
      f=factorial(x)
      if f%n==0:
        return x
        
def factorial(n):
  return n<2 or n*factorial(n-1)
​
def isItPrime(n):
  sq=round(math.sqrt(n)+1)
  for x in range(2,sq):
  
    if n%x==0:
      return False
    
  return True

