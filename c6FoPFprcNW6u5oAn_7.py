"""


The Farey sequence of order `n` is the set of all fractions with a denominator
between 1 and `n`, reduced and returned in ascending order. Given `n`, return
the Farey sequence as a list, with each fraction being represented by a string
in the form "numerator/denominator".

### Examples

    farey(1) ➞ ["0/1", "1/1"]
    
    farey(4) ➞ ["0/1", "1/4", "1/3", "1/2", "2/3", "3/4", "1/1"]
    
    farey(5) ➞ ["0/1", "1/5", "1/4", "1/3", "2/5", "1/2", "3/5", "2/3", "3/4", "4/5", "1/1"]

### Notes

The Farey sequence will always begin with "0/1" and end with "1/1".

"""

from fractions import Fraction
from itertools import combinations as com
def farey(n):
  fractions = list(com([x for x in range(1,n+1)],2))
  Frac = []
  for n,d in fractions:
    if Fraction(n,d) not in Frac:
      Frac.append((Fraction(n,d)))
  Frac.sort()
  Frac.append("1/1")
  return ["0/1"] + [str(x) for x in Frac]

