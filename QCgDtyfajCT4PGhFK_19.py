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
  i = 2
  factors = []
  while i * i <= number:
    if number % i:
      i += 1
    else:
      number //= i
      factors.append(i)
  if number > 1:
    factors.append(number)
  return factors

