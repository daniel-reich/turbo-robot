"""


A list is **positive dominant** if it contains **strictly more** **unique**
positive values than **unique** negative values. Write a function that returns
`True` if a list is **positive dominant**.

### Examples

    is_positive_dominant([1, 1, 1, 1, -3, -4]) ➞ False
    # There is only 1 unique positive value (1).
    # There are 2 unique negative values (-3, -4)
    
    is_positive_dominant([5, 99, 832, -3, -4]) ➞ True
    
    is_positive_dominant([5, 0]) ➞ True
    
    is_positive_dominant([0, -4, -1]) ➞ False

### Notes

`0` counts as neither a positive nor a negative value.

"""

def is_positive_dominant(lst):
  pos = 0
  pos_nums = []
  neg = 0
  neg_nums = []
  for i in lst:
    if i > 0 and i not in pos_nums:
      pos += 1
      pos_nums.append(i)
    elif i < 0 and i not in neg_nums:
      neg += 1
      neg_nums.append(i)
  return pos > neg
