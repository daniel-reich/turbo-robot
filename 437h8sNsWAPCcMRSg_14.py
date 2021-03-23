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

def is_prime(num):
  for factor in range(2,num):
    if num%factor==0:
        return False
  return True
      
primes = [entry for entry in range(2,1000) if is_prime(entry)]
print(primes)
​
​
def divisible(num):
  for prime in primes:
      divided = num/prime
      if int(divided) == divided:
        return divided
​
  return "not divisible"
​
def product_of_primes(num):
  print(num)
  if divisible(num)=="not divisible":
    return False
  else:
    print(divisible(num))
    if divisible(num) in primes:
      return True
  
  return False

