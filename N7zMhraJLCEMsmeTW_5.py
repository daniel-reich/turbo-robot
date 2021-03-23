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
  type_a=''.join('1' if i%2 else '0' for i in range(len(string)))
  type_b=''.join('0' if i%2 else '1' for i in range(len(string)))
  return min(sum(not type_a[i]==string[i] for i in range(len(string))),sum(not type_b[i]==string[i] for i in range(len(string))))

