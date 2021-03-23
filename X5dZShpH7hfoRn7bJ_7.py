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
    if n == 1 or k == 1 or n-k == 1 or n < k:
        return False
    elif n == k:
        return True
    elif n % k == 0:
        return True
    missing = n - k
    check = 0
    primes = get_primes(n)
    if k == get_sum(primes) or missing == get_sum(primes):
        return True
    for i in range(len(primes)):
        if k % primes[i] == 0 and missing % primes[i] == 0:
            check += 1
    if check == 0:
        return False
    else:
        return True
​
​
def get_primes(n):
    primes = []
    count = 0
    for i in range(2, n-2):
        if n % i == 0:
            for j in range(2, i-1):
                if i % j == 0:
                    count += 1
            if count == 0:
                primes.append(i)
    return primes
​
​
def get_sum(primes):
    total = 0
    for i in range(len(primes)):
        total += primes[i]
    return total

