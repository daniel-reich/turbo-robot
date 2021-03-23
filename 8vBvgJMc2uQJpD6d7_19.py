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
  factors = []
  target_num = num
  i = 2
  while(i <= target_num):
    if(target_num % i == 0):
      factors.append(i)
      target_num /= i
      i = 2
    else:
      i += 1
  return factors

