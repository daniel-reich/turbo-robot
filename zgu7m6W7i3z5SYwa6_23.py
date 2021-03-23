"""


Write a function that takes a list of two numbers and determines if the sum of
the **digits** in each number are equal to each other.

### Examples

    is_equal([105, 42]) ➞ True
    # 1 + 0 + 5 = 6
    # 4 + 2 = 6
    
    is_equal([21, 35]) ➞ False
    
    is_equal([0, 0]) ➞ True

### Notes

N/A

"""

import textwrap
def is_equal(lst):
  return sum([int(i) for i in textwrap.wrap(str(lst[0]),1)])==sum([int(j) for j in textwrap.wrap(str(lst[1]),1)])

