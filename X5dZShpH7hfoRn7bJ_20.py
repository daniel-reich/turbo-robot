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

import itertools
def c_fuge(n, k):
    if k == 1 or k == n - 1:
        return False
    elif n == k:
        return True
    lst = get_primes(n)
    return send(lst,n,k)
​
import itertools
def c_fuge(n, k):
    if k == 1 or k == n - 1:
        return False
    if n == k:
        return True
    lst = get_primes(n)
    return send(lst,n,k)
​
def send(lst,n,k):
    a = 0
    cay = 0
    minus = 0
    while a < k:
        a += 1
        for i in itertools.combinations_with_replacement(lst,a):
            if sum(i) == k:
                cay += 1
            if sum(i) == (n - k):
                minus += 1
            if cay >= 1 and minus >= 1:
                return True
    return False
​
def is_prime(x):
    lst = 0
    for i in range(2,x):
        if x % i == 0:
            lst += 1
            break
    return True if lst == 0 else False
​
def get_primes(x):
    lst=[]
    for i in range(2,x):
        if x % i == 0:
            if is_prime(i):
                lst.append(i)
    return lst

