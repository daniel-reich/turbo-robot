"""


Write a function that takes a list of elements and returns only the integers.

### Examples

    return_only_integer([9, 2, "space", "car", "lion", 16]) ➞ [9, 2, 16]
    
    return_only_integer(["hello", 81, "basketball", 123, "fox"]) ➞ [81, 123]
    
    return_only_integer([10, "121", 56, 20, "car", 3, "lion"]) ➞ [10, 56, 20, 3]
    
    return_only_integer(["String",  True,  3.3,  1]) ➞ [1]

### Notes

N/A

"""

def return_only_integer(lst):
  lstint = []
  for s in lst:
    if type(s) == int:
      lstint.append(s)
  return lstint

