"""


Given `num` as input, return a list with all primes up to `num` included.

![Alternative Text](https://edabit-
challenges.s3.amazonaws.com/Sieve_of_Eratosthenes_animation.gif)

### Examples

    eratosthenes(1) ➞ []
    
    eratosthenes(10) ➞ [2, 3, 5, 7]
    
    eratosthenes(20) ➞ [2, 3, 5, 7, 11, 13, 17, 19]
    
    eratosthenes(0) ➞ []

### Notes

  * Check the **Resources** tab for info on the meaning of "Eratosthenes".
  * Try solving this challenge using Eratosthenes sieve.

"""

def is_prime(n):
  if n >= 2:
    for y in range(2, n):
      if not (n % y):
        return False
  else:
    return False
  return True
def filter_primes(num):
  return list(filter(is_prime, num))
def eratosthenes(num):
  
  return filter_primes(list(range(num)))

