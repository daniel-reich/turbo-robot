"""


Create a function that takes two integers and returns `true` if a digit
repeats three times in a row at any place in `num1` **AND** that same digit
repeats two times in a row in `num2`.

### Examples

    trouble(451999277, 41177722899) ➞ True
    
    trouble(1222345, 12345) ➞ False
    
    trouble(666789, 12345667) ➞ True
    
    trouble(33789, 12345337) ➞ False

### Notes

You can expect every test case to contain exactly two integers.

"""

import re
def trouble(num1, num2):
  str1=str(num1)
  str2=str(num2)
  for d in str1:
    if d+d+d in str1:
      if d+d in str2:
        return True
  return False

