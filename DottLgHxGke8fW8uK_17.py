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

def nPr(n, r):
  ans = 1
  for i in range(r):
    ans*= (n-i)
  return ans
​
def nCr(n, r):
  r = min(r,n-r)
  ans = nPr(n,r)
  for i in range(1,r+1):
    ans//= i
  return ans

