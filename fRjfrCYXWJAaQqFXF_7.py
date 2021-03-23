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

from itertools import count, islice
from functools import reduce
​
def primorial(n):
    primes = (n for n in count(2) if all(n%d for d in range(2, n)))
    return reduce(lambda a,b: a*b, islice(primes, 0, n))

