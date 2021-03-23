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

def is_prime(n):
  return n>1 and all(n%i for i in range(2, int(n**0.5)+1))
def prime_divisors(num):
  A=[x for x in range(1, num+1) if num%x==0]
  return [x for x in A if is_prime(x)]

