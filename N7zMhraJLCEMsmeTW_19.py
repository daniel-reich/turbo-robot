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

from itertools import cycle
​
​
def matcher(txt, cycle):
  return sum(
    i != next(cycle)
    for i, _ in zip(txt, range(len(txt)))
  )
​
​
def min_swaps(string):
  cycles = (cycle('01'), cycle('10'))
  return min(matcher(string, i) for i in cycles)

