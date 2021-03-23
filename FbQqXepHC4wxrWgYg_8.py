"""


Given a number, return all its prime divisors in a list. Create a function
that takes a number as an argument and returns all its prime divisors.

  * n = 27
  * All divisors: `[3, 9, 27]`
  * Finally, from that list of divisors, return the prime ones: `[3]`

### Examples

    prime_divisors(27) ➞ [3]
    
    prime_divisors(99) ➞ [3, 11]
    
    prime_divisors(3457) ➞ [3457]

### Notes

N/A

"""

def prime_divisors(num):
  def divisors(num):
    factors = []
    for n in range(1, num//2 + 1):
      if num % n == 0:
        factors.append(n)
        factors.append(num//n)
    return factors
  def is_prime(num):
    if num <= 1:
      return False
    for n in range(2, num):
      if num % n == 0:
        return False
    return True
  
  return sorted([n for n in list(set(divisors(num))) if is_prime(n) == True])

