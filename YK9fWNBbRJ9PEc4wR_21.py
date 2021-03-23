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
  n=[]
  n.append(lst1[0])
  for a in range(0,len(lst2)):
    n.append(lst2[a])
  n.append(lst1[1])
  return n

