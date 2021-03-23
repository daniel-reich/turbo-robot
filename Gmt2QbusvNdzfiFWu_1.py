"""


Create a function that takes a list of positive integers and returns a string
as:

  *  **p1** , **sum of all ij** of the list for which **p1** is a prime factor.
  *  **p2** , **sum of all ij** of the list for which **p2** is a prime factor, **...** .
  *  **pn** , **sum of all ij** of the list for which **pn** is a prime factor.

### Examples

    sum_prime([12, 15]) ➞ "(2 12)(3 27)(5 15)"
    # 2 is a prime factor of 12 results (2 12).
    # 3 is a prime factor of 12 and 15, add 15 + 12, results (3 27).
    # 5 is a prime factor of 15 results (5 15).
    # 7, 11 and 13 are prime numbers but not a factor of any of the number
    # in the given list.
    
    sum_prime([7, 13, 18, 23, 24]) ➞ "(2 42)(3 42)(7 7)(13 13)(23 23)"
    
    sum_prime([3, 5, 7, 9, 11, 13]) ➞ "(3 12)(5 5)(7 7)(11 11)(13 13)"

### Notes

N/A

"""

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]
​
primes = primes2(10**3)
​
def sum_prime(lst):
    ans = ""
    m = max(lst)
    for p in primes:
        if p > m:
            break
        A = [k for k in lst if k % p == 0]
        if len(A) > 0:
            ans += "(" + str(p) + " " + str(sum(A)) + ")"
    return ans

