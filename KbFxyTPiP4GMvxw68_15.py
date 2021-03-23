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

def longest_zero(s):
  import re
  lst = re.findall(r'0+', s)
  return sorted(lst, key = len, reverse = True)[0] if len(lst) else ''

