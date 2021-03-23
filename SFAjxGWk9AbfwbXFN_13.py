"""


Create a function that will find all primes below a given number. Return the
result as a list.

### Examples

    primes_below_num(5) ➞ [2, 3, 5]
    
    primes_below_num(10) ➞ [2, 3, 5, 7]
    
    primes_below_num(20) ➞ [2, 3, 5, 7, 11, 13, 17, 19]

### Notes

If `n` is a prime, it is included in the list.

"""

def primes_below_num(n):
  def is_prime(m):
    if m >= 2:
      for y in range(2, m):
        if not (m % y):
          return False
    else:
      return False
    return True
  nums = []
  for i in range(n+1):
    nums.append(i)
  def filter_primes(nums):
    return list(filter(is_prime, nums))
  return filter_primes(nums)

