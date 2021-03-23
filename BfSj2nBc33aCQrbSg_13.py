"""


A left-truncatable prime is a prime number that contains no 0 digits and, when
the first digit is successively removed, the result is always prime.

A right-truncatable prime is a prime number that contains no 0 digits and,
when the last digit is successively removed, the result is always prime.

Create a function that takes an integer as an argument and:

  * If the integer is only a left-truncatable prime, return `"left"`.
  * If the integer is only a right-truncatable prime, return `"right"`.
  * If the integer is both, return `"both"`.
  * Otherwise, return `False`.

### Examples

    truncatable(9137) ➞ "left"
    # Because 9137, 137, 37 and 7 are all prime.
    
    truncatable(5939) ➞ "right"
    # Because 5939, 593, 59 and 5 are all prime.
    
    truncatable(317) ➞ "both"
    # Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.
    
    truncatable(5) ➞ "both"
    # The trivial case of single-digit primes is treated as truncatable from both directions.
    
    truncatable(139) ➞ False
    # 1 and 9 are non-prime, so 139 cannot be truncatable from either direction.
    
    truncatable(103) ➞ False
    # Because it contains a 0 digit (even though 103 and 3 are primes).

### Notes

The input integers will not exceed 10^6.

"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:40:52 2020
​
@author: fabin
"""
​
​
def prime(n):
  if n == 1:
    return False
  for i in range(2,((n//2)+1)):
    if n%i == 0:
      return False
  return True
    
def truncatable(n):
  if not prime(n):
    return False
  left = True
  right = True
  n_str = str(n)
  while len(n_str)>1 and left:
    n_list = []
    for i in range(1,len(n_str)):
      n_list.append(n_str[i])
    str2 = n_list[0]
    if '0' in n_list:
      left = False
      right = False
    for i in range(1,len(n_list)):
      str2 = str2 + n_list[i]
    n_left = int(str2)
    if not prime(n_left):
      left = False
    n_str = str(n_left)
  n_str = str(n)
  while len(n_str)>1 and right:
    n_list = []
    for i in range(0,(len(n_str)-1)):
      n_list.append(n_str[i])
    str2 = n_list[0]
    for i in range(1,len(n_list)):
      str2 = str2 + n_list[i]
    n_right = int(str2)
    if not prime(n_right):
      right = False
    n_str = str(n_right)
  if left and not right:
    return "left"
  elif right and not left:
    return "right"
  elif left and right:
    return "both"
  else:
    return False

