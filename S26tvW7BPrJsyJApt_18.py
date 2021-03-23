"""


Write a function that takes a list and a number as arguments. Add the number
to the end of the list, then remove the first element of the list. The
function should then return the updated list.

### Examples

    next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
    
    next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
    
    next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
    
    next_in_line([], 6) ➞ "No list has been selected"

### Notes

For an empty list input, return: `"No list has been selected"`

"""

def next_in_line(lst, num):
  if not lst:
    return 'No list has been selected'
  else:
    lst.append(num)
    lst.pop(0)
  return lst

