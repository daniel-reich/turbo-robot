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

def min_swaps(s):
​
  swps0 = sum( 1 for i in range(len(s)) if s[i] != '0101010101'[i]   )
  swps1 = sum( 1 for i in range(len(s)) if s[i] != '0101010101'[i+1] )
​
  return min(swps1,swps0)

