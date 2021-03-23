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

import itertools
​
def trouble(num1, num2):
  d = ({int(k):len(list(g)) for k,g in itertools.groupby(str(num1))})
  try:
    min_v = list(d.keys())[list(d.values()).index(3)]
  except:
    return False
    
  for k,g in itertools.groupby(str(num2)):
    l = sum(1 for x in list(g))
    if l >= 2 and int(k) == min_v:
      return True
  return False

