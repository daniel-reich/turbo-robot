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

def is_prime(num):
  if num == 2 or num == 3:
    return True
  elif num < 2 or num % 2 == 0 or num % 3 == 0:
    return False
  for divisor in range(5, num // 2 + 1):
    if num % divisor == 0:
      return False
  return True
​
def prime_divisors(num):
  divisors_prime = []
  for divisor in range(2, num // 2 + 1):
    if num % divisor == 0 and is_prime(divisor):
      divisors_prime.append(divisor)  
  return divisors_prime

