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

def get_prime_factor(num):
  for x in range(2, num+1):
    if num % x == 0:
      return x
​
def prime_factors(num):
  res = []
  
  while 1:
    x = get_prime_factor(num)
    if not x:
      break
    res.append(x)
    num = num // x
    
  return res

