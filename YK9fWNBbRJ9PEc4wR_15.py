"""


Create a function that takes two lists and insert the second list in the
middle of the first list.

### Examples

    tuck_in([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    tuck_in([15,150], [45, 75, 35]) ➞ [15, 45, 75, 35, 150]
    
    tuck_in([[1, 2], [5, 6]], [[3, 4]]) ➞ [[1, 2], [3, 4], [5, 6]]

### Notes

The first list always has two elements.

"""

def tuck_in(lst1, lst2):
  a = round(len(lst1)/2)
  nlst1 = lst1[:a]
  nlst2 = lst1[a:]
  nlst1.extend(lst2)
  nlst1.extend(nlst2)
  return nlst1

