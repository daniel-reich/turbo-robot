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
  if number == 1:
    return []
  lst = []
  i = 2
  while(i<=number and i > 1):
    if number % i == 0:
      number /= i
      lst.append(i)
      i = 2
      continue
    i += 1
  return lst

