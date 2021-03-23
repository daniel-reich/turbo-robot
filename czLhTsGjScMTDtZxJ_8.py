"""


In mathematics, primorial, denoted by “#”, is a function from natural numbers
to natural numbers similar to the factorial function, but rather than
successively multiplying positive integers, the function only multiplies
**prime numbers**.

Create a function that takes an integer `n` and returns its **primorial**.

### Examples

    primorial(1) ➞ 2
    # First prime number = 2
    
    primorial(2) ➞ 6
    # Product of first two prime numbers = 2*3 = 6
    
    primorial(6) ➞ 30030

### Notes

n >= 1.

"""

def primorial(n):
  count = 0
  fin = 1
  cur = 2
  while count<n:
    if is_prime(cur):
      count+=1
      fin*=cur
    cur+=1
  return fin
​
def is_prime(n):
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

