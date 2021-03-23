"""


Write a function that returns `True` if the given number `num` is a product of
any two prime numbers.

### Examples

    product_of_primes(2059) ➞ True
    # 29*71=2059
    
    product_of_primes(10) ➞ True
    # 2*5=10
    
    product_of_primes(25) ➞ True
    # 5*5=25
    
    product_of_primes(999) ➞ False
    # There are no prime numbers.

### Notes

  * `num` is always greater than 0.
  * `0` and `1` aren't prime numbers.

"""

def product_of_primes(num):
  a,n=0,2
  p=[x for x in range(num) if all(x%i for i in range(2,x))]
  while n<len(p):
    for m in range(n,len(p)):
      if p[n]*p[m]==num:
        a=a+1
    n=n+1
  return a!=0

