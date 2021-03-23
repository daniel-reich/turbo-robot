"""


Write a function that returns the extended form of the prime factorization of
a number. Return in the format `[a, b, c, d, ...]`, where each element of the
list is an integer.

### Examples

    prime_factorization(216) ➞ [2, 2, 2, 3, 3, 3]
    
    prime_factorization(64) ➞ [2, 2, 2, 2, 2, 2]
    
    prime_factorization(23) ➞ [23]

### Notes

N/A

"""

def prime_factorization(number):
  primes = [2,3]
  arr = []
  for i in range(4,number-1):
    if is_prime(i):
      primes.append(i)
  while number > 1:
    for x in primes:
      if number % x == 0:
        number /= x
        arr.append(x)
  return sorted(arr)
    
def is_prime(num):
  if num > 1:
    for i in range(2,num):
      if num % i == 0:
        return False
    return True
  else : return True

