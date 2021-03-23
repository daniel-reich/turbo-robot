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

primes=[2]
def primorial(n):
  a,product=1,1
  while len(primes)<n:
    lp=primes[-1]
    for i in range(lp+1+100*(a-1),lp+1+100*a):
      if all(i%p for p in primes):
        primes.append(i)
    if lp==primes[-1]:
      a+=1
    else:
      a=1
  for p in primes[:n]:
    product*=p
  return product

