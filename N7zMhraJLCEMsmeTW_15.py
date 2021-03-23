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
  chars = list(string)
  copy = chars[:]
  count1 = 0
  count2 = 0
  for i in range(len(string)-1):
    if chars[i] == chars[i+1]:
      count1 += 1
      if chars[i] == '1':
        chars[i+1] = '0'
      else:
        chars[i+1] = '1'
  rev = copy[::-1]
  for i in range(len(rev)-1):
    if rev[i] == rev[i+1]:
      count2 += 1
      if rev[i] == '1':
        rev[i+1] = '0'
      else:
        rev[i+1] = '1'
  if count1 <= count2:
    return count1
  else:
    return count2

