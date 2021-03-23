"""


Create a function that returns the next element in an **arithmetic sequence**.
In an arithmetic sequence, each element is formed by adding the same constant
to the previous element.

### Examples

    next_element([3, 5, 7, 9]) ➞ 11
    
    next_element([-5, -6, -7]) ➞ -8
    
    next_element([2, 2, 2, 2, 2]) ➞ 2

### Notes

All input arrays will contain **integers only**.

"""

def next_element(lst):
  if lst[0] == lst[1]:
    return lst[0]
  elif lst[0] > lst[1]:
    x = lst[0] - lst[1]
    return (lst[-1]-x)
  else:
    x = lst[1] - lst[0]
    return (lst[-1]+x)

