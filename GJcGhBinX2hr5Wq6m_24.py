"""


Create a function that takes a list `lst` of numbers and **moves all zeros to
the end** , preserving the order of the other elements.

### Examples

    move_zeros([1, 0, 1, 2, 0, 1, 3]) ➞ [1, 1, 2, 1, 3, 0, 0]
    
    move_zeros([0, 1, None, 2, false, 1, 0]) ➞ [1, None, 2, false, 1, 0, 0]
    
    move_zeros(['a', 0, 0, 'b', 'c', 'd', 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) ➞ ['a', 'b', 'c', 'd', 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

### Notes

N/A

"""

def move_zeros(lst):
  return [i for i in lst if str(i) not in ['0', '0.0']] + [j for j in lst if str(j) in ['0', '0.0']]

