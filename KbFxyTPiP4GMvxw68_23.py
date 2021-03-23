"""


Write a function that returns the longest sequence of consecutive zeroes in a
binary string.

### Examples

    longest_zero("01100001011000") ➞ "0000"
    
    longest_zero("100100100") ➞ "00"
    
    longest_zero("11111") ➞ ""

### Notes

If no zeroes exist in the input, return an empty string.

"""

import re 
​
def longest_zero(s):
  st = sorted(re.findall(r'[0]+', s), key=len)
  return st[-1] if len(st) else ''

