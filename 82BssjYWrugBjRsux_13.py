"""


Return the sum of all items in a list, where each item is multiplied by its
index (zero-based). For empty lists, return `0`.

### Examples

    index_multiplier([1, 2, 3, 4, 5]) ➞ 40
    # (1*0 + 2*1 + 3*2 + 4*3 + 5*4)
    
    index_multiplier([-3, 0, 8, -6]) ➞ -2
    # (-3*0 + 0*1 + 8*2 + -6*3)

### Notes

All items in the list will be integers.

"""

def index_multiplier(lst):
  return sum([idx*x for idx, x in enumerate(lst)])

