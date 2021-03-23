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

def is_prime (n):
  for x in range (2,n):
    if n%x==0:
      return False
  return True
​
def prime_factorization(number):
  lista=[]
  for x in range (2,number+1):
    if is_prime(x):
      while number%x==0:
        lista.append(x)
        number=number//x
  return lista

