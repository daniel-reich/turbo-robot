"""


A centrifuge, as you probably know, is a laboratory device used to separate
fluids based on density. The separation is achieved through centripetal force
by spinning a collection of test tubes at high speeds. This means, the
configuration needs to be in balance.

Create a function that takes two numbers as arguments `n` and `k` and returns
`True` if the configuration is balanced and `False` if it's not. To check out
the formula, look at the **resources tab**.

![The Centrifuge Problem with 6 Holes, n=6](https://edabit-
challenges.s3.amazonaws.com/6_hole_centrifuge.png)

Here are the valid configurations for _n_ = 6, _k_ = 2, 3, 4 and 6.

### Examples

    c_fuge(6, 4) ➞ True
    
    c_fuge(2, 1) ➞ False
    
    c_fuge(3, 3) ➞ True

### Notes

  * One test tube `k = 1` is **never** in balance.
  * One hole `n = 1` is **never** in balance, even empty.

"""

def c_fuge(n, k):
  def prime_finder(n):
    primes = []
​
    for num in range(2, n + 1):
      if len(primes) == 0:
        primes.append(num)
      else:
        prime = True
        for item in primes:
          r = num % item
​
          if r == 0:
            prime = False
            break
        
        if prime == True:
          primes.append(num)
    
    return primes
  def prime_divisors(n, primes):
    
    p_divs = []
​
    for prime in primes:
      r = 0
      while r == 0:
        r = n % prime
​
        if r == 0:
          p_divs.append(prime)
          n = n/prime
    
    return p_divs
  def can_be_added(n, primes):
    
    primes = sorted(primes)
    orig_n = n
​
    m = min(primes)
    
    for prime in primes:
      r = n % prime
​
      if r == 0:
        return True
    for index in range(1, len(primes) + 1):
      prime = primes[-index]
      
      while n >= prime:
        n -= prime
        div = False
        
        for p in primes:
          r = n % p
​
          if r == 0:
            div = n / p, p
        
        if div != False:
          for num in range(0, int(div[0])):
            n -= int(div[1])
        
        
    
    if n == 0:
      return True
    else:
      return False
  
  if n == 1 or k == 1 or k > n:
    return False
  
  pfn = prime_finder(n)
  pdn = prime_divisors(n, pfn)
  pdn = set(pdn)
​
  d = n - k
​
  kadd = can_be_added(k, pdn)
  dadd = can_be_added(d, pdn)
​
  if kadd == True and dadd == True:
    return True
  else:
    return False

