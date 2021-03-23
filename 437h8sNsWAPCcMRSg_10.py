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

def ss(a):
  f=True
  for i in range(2,a):
    if a%i==0:
      f=False
  if a==1:
    f=False
  return f
def product_of_primes(num):
  a=2
  while a<num:
    if ss(a):
      if num%a==0:
        if ss(int(num/a)):
          return True
          break
    a+=1
  if a==num:
    return(False)

