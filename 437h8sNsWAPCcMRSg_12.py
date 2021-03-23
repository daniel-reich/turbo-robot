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

primes = [2]
def prime(v):
    for den in range(2, v):
        if((v // den) == (v / den)):
            return False
    return True
​
def updatePrimes(v):
    global primes
        
    if (v > primes[-1]):
        for num in range(primes[-1] + 1, v + 1):
            if(prime(num)):
                primes.append(num)
                    
def product_of_primes(num):
    updatePrimes(num)
    for n1 in primes:
        if(n1 >= num):
            return False
        for n2 in primes:
            if(n2 >= num):
                return False
​
            prod = n1 * n2
            if(prod > num):
                break
            if(prod == num):
                return True
    return False

