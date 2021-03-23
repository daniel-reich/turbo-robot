"""


A _Primorial_ is a product of the first `n` prime numbers (e.g. `2 x 3 x 5 =
30`). `2, 3, 5, 7, 11, 13` are prime numbers. If `n` was `3`, you'd multiply
`2 x 3 x 5 = 30` or Primorial = `30`.

Create a function that returns the Primorial of a number.

### Examples

    primorial(1) ➞ 2
    
    primorial(2) ➞ 6
    
    primorial(8) ➞ 9699690

### Notes

N/A

"""

from operator import mul
from functools import reduce
​
is_prime = lambda n: n > 1 and all(n%i for i in range(2, int(n**0.5 + 1)))
​
def first_n_primes(n):
    '''
    Returns each of the first n prime numbers one at a time
    '''
    p = 2
    for _ in range(n):
        yield p
        p += 1
        while not is_prime(p):
            p += 1
​
PRIMES = list(first_n_primes(10))
​
primorial = lambda n: reduce(mul,PRIMES[:n])

