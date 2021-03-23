"""


A prime gap of length n is a run of n-1 consecutive composite numbers between
two successive primes. See this
[Resource](https://mathworld.wolfram.com/PrimeGaps.html) for more information.

The prime numbers are not regularly spaced. For example gap between:

  * 2 and 3 is 1
  * 3 and 5 is 2
  * 7 and 11 is 4

Create a function with following parameters:

    g (integer >= 2)
    # Gap between the consecutive primes
    
    a (integer > 2)
    # Start of the search (a inclusive)
    
    b (integer >= a)
    # End of the search (b inclusive)

... and returns the first pair of two prime numbers spaced with a gap of **g**
between the limits **a and b**.

    prime_gaps(2, 3, 50) ➞ [3, 5]
    
    # Between 2 and 50 we have following pairs of 2-gaps primes:
    # 3-5, 5-7, 11-13, 17-19, 29-31, 41-43.
    
    # [3, 5] is the first pair between 3 and 50 with a 2-gap.

### Examples

    prime_gaps(2, 5, 7) ➞ [5, 7]
    
    prime_gaps(2, 5, 5) ➞ None
    
    prime_gaps(4, 130, 200) ➞ [163, 167]

### Notes

Return `None` if consecutive prime numbers are not found with the required
gap.

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
primes = primes2(10**6)
​
def prime_gaps(g, a, b):
    for i in range(len(primes) - 1):
        p1, p2 = primes[i:i+2]
        if p1 >= a and p2 <= b and p2 - p1 == g:
            return [p1, p2]
        if p1 + g > b:
            break
    return None

