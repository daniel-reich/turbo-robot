"""


Create a function that finds a target number in a list of prime numbers.
Implement a **binary search algorithm** in your function. The target number
will be from 2 through 97. If the target is prime then return `"yes"` else
return `"no"`.

### Examples

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    is_prime(primes, 3) ➞ "yes"
    
    is_prime(primes, 4) ➞ "no"
    
    is_prime(primes, 67) ➞ "yes"
    
    is_prime(primes, 36) ➞ "no"

### Notes

  * You could use built-in functions to solve this, but the point of this challenge is to see if you understand the **binary search algorithm**.
  * The solution is in the **Resources** tab.

"""

from math import floor
​
def is_prime(primes, num, left=0, right=None):
    n = len(primes)
    L = 0
    R = n-1
    while L <= R:
      mid = floor((L+R)/2)
      if primes[mid] < num:
        L = mid + 1
      elif primes[mid] > num:
        R = mid - 1
      else:
        return 'yes'
    return 'no'

