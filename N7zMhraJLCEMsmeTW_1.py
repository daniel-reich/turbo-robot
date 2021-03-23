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

def min_swaps(string):
  com1 = "101010101010101010"[:len(string)]
  com2 = "010101010101010101"[:len(string)]
  i1,i2 = 0, 0
  for s,c1,c2 in zip(string,com1,com2):
    if s != c1: i1 += 1
    if s != c2: i2 += 1
  return min([i1,i2])

