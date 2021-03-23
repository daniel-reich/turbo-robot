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

def is_equal(lst):
  total = []
  for x in lst:
    totalsum = 0
    for y in str(x):
      totalsum += int(y)
    total.append(totalsum)
  if len(total) == total.count(total[0]):
    return True
  else:
    return False

