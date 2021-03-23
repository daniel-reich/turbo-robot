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
  zero_counter = 0
  counter_lst = []
  
  for digit in s:
    if digit == '0':
      zero_counter += 1
      counter_lst.append(zero_counter)
    else:
      zero_counter = 0
  
  return '0' * max(counter_lst) if len(counter_lst) >= 1 else ""

