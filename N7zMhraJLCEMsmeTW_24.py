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
  first_odd, first_even = [], []
  for i in range(len(string)):
    first_odd += "1" if i % 2 == 0 else "0"
    first_even += "0" if i % 2 == 0 else "1"
  
  diff_f_odd = [1 for a, b in zip(first_odd, list(string)) if a != b]
  diff_f_even = [1 for a, b in zip(first_even, list(string)) if a != b]
​
  return min((sum(diff_f_odd), sum(diff_f_even)))

