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

def is_prime(numb):
  lst = [x for x in range(2,numb)]
  for j in lst:
    if numb % j == 0:
      return False
    elif numb % j != 0 and j == numb - 1:
      return True
​
def product_of_primes(num):
  factors =  [x for x in range(1,num+1) if num % x == 0]
  if len(factors) % 2 !=0:
    factors.insert(factors.index(factors[int(len(factors))//2])+1,factors[int(len(factors))//2])
  first = factors[:int(len(factors)/2)]
  second = [x for x in reversed(factors[int(len(factors)/2):])]
  i = 0
  while i < len(first):
    if is_prime(first[i]) is True and is_prime(second[i]) is True:
      return True
    i = i + 1
  return False

