"""


Write a function that efficiently calculates **nPr** (number of permutations
of `r` items from a set of size `n`) and another function that efficiently
calculates **nCr** (number of combinations of `r` items from a set of size
`n`, regardless of order).

  * The formula for calculating nPr is `n!/(n-r)!` (`"!"` is the factorial operation).
  * The formula for calculating nCr is `n!/(r!(n-r)!)`.

Your functions should work efficiently for cases where `n!` or `r!` are very
large compared to the result. Simply calculating the factorials and dividing
will cause your program to time out. See if you can think of a more efficient
method.

### Examples

    # Permutations
    
    nPr(7, 4) ➞ 840
    nPr(300, 3) ➞ 26730600
    
    # Combinations
    
    nCr(7, 4) ➞ 35
    nCr(300, 3) ➞ 4455100
    nCr(300, 297) ➞ 4455100

### Notes

  * `n` and `r` will always be positive integers where `n` >= `r`.
  * Think about what factors will cancel out when dividing the factorials.

"""

from math import factorial, log2
nPr = lambda n, r: round(2 ** sum([log2(n - i) for i in range(r)]))
​
nCr = lambda n, r: round(nPr(n, min(r, n - r)) / factorial(min(r, n - r)))

