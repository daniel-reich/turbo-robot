"""


Create a function that returns the minimum number of **swaps** it takes to
transform a **binary string** into a string of **alternating 0s and 1s**. A
swap is switching from a 0 to a 1 or vice versa.

### Examples

    min_swaps("010010111") ➞ 4
    
    # Two possible conversions:
    #   1. "101010101" (4 swaps)
    #   2. "010101010" (5 swaps)
    
    min_swaps("10101010") ➞ 0
    
    min_swaps("10010") ➞ 2

### Notes

N/A

"""

def min_swaps(st):
  l = len(st)
  t1, t2 = '01', '10'
  s = sum(st[x]!= t1[x%2] for x in range(l))
  s2 = sum(st[x]!= t2[x%2] for x in range(l))
  return min(s,s2)

