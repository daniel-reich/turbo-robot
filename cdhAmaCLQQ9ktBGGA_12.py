"""


Create a function that takes a list with numbers and return a list with the
elements multiplied by two.

### Examples

    get_multiplied_list([2, 5, 3]) ➞ [4, 10, 6]
    
    get_multiplied_list([1, 86, -5]) ➞ [2, 172, -10]
    
    get_multiplied_list([5, 382, 0]) ➞ [10, 764, 0]

### Notes

N/A

"""

def get_multiplied_list(lst):
  return [i * 2 for i in lst]

