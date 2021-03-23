"""


Create a function which _simplifies_ a given **fraction** into its **simplest
ratio**. Return the fraction as a _string_.

### Examples

    simplify_frac("2/4") ➞ "1/2"
    
    simplify_frac("15/25") ➞ "3/5"
    
    simplify_frac("4/9") ➞ "4/9"

### Notes

  * Fractions are given as strings.
  * Return the same fraction if it is already in its simplified ratio (see example #3).

"""

def simplify_frac(f):
  first = int(f[:f.index("/")])
  second = int(f[f.index("/")+1:])
  i = first
  while i > 0:
    if first % i == 0 and second % i == 0:
      first /= i
      second /= i
    i -= 1
  return str(int(first)) + "/" + str(int(second))

