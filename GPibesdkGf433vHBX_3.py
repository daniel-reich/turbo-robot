"""


[Goldbach's Conjecture](https://en.wikipedia.org/wiki/Goldbach%27s_conjecture)
is amongst the oldest and well-known unsolved mathematical problems. In
correspondence with [Leonhard
Euler](https://en.wikipedia.org/wiki/Leonhard_Euler) in 1742, German
mathematician [Christian
Goldbach](https://en.wikipedia.org/wiki/Christian_Goldbach) made a conjecture,
which states:

 **"Every even whole number greater than 2 is the sum of two prime numbers."**

Even though it's been thoroughly tested and analyzed and seems to be true, it
hasn't been proved yet (thus, remaining a conjecture.)

Create a function that takes a number and returns an array as per the
following rules:

  * If the given number is odd and greater than two, return an empty array.
  * If the given number is even and greater than two, return an array of two prime numbers whose sum is the given input.
  * Both prime numbers must be the farthest (with the greatest difference).

### Examples

    goldbach_conjecture(1) ➞ []
    # The given number is not greater than 2.
    
    goldbach_conjecture(7) ➞ []
    # The given number is not an even number.
    
    goldbach_conjecture(14) ➞ [3, 11]

### Notes

Return list in sequence: `[smaller, bigger]`

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
primes = primes2(10000)
​
def goldbach_conjecture(n):
    if n % 2 == 1 or n < 4:
        return []
    for p in primes:
        if n - p in primes:
            return [p, n-p]

