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
  def ip(x):
    return all(x%y for y in range(2,(x//2)+1))
​
  l = []
  while not ip(num):
    for x in (y for y in range(2,(num//2)+1) if ip(y)):
      if not num % x:
        l.append(x)
        num //= x
        break
  l.append(num)
  return l

