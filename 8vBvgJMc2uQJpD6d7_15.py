"""


Create a function that returns a list containing the prime factors of whatever
integer is passed to it.

### Examples

    prime_factors(20) ➞ [2, 2, 5]
    
    prime_factors(100) ➞ [2, 2, 5, 5]
    
    prime_factors(8912234) ➞ [2, 47, 94811]

### Notes

  * Implement your solution using trial division.
  * Your solution should not require recursion.

"""

def prime_factors(num):
  lst = list()
  first_factor = 2
  while num > 1:
    if num%first_factor == 0:
      lst.append(first_factor)
      num /= first_factor
    else:
      first_factor += 1
  
  return lst

