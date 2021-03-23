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

def is_prime(n):
  return sum(1 for x in range(2,n+1) if n%x==0 )==1
def primorial(n):
  cont,pn,prime=0,2,1
  while cont<n:
    if is_prime(pn):
      prime=prime*pn
      pn+=1
      cont+=1
    else: pn+=1
  return prime

