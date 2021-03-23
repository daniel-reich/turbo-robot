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
  if n==1: return 2
  a = []
  for i in range(2, n**2):
    for j in range(2, i):
      if i%j==0:
        break
    else: a.append(i)
  return eval("*".join(str(i) for i in a[:n]))

