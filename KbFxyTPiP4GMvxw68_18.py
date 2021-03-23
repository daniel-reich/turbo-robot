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
  count = 0
  if '0' not in s:
    return ''
  while count < len(s):
    if s[0] == '0':
      count = max(count, s.find('1'))
    try:
      s = s[s.index('1') + 1:]
    except ValueError:
      count = max(len(s), count)
      s = s[s.find('1')]
  return '0' * count

