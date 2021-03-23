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
  return n>1 and all(n%i for i in range(2,int(n**.5)+1))
def primorial(n):
  i=0
  c=0
  p=1
  while c<n:
    i+=1
    if is_prime(i):
      c+=1
      p*=i
  return p

