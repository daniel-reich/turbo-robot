"""


Create a function that takes in two lists and returns `True` if the second
list follows the first list by **one** element, and `False` otherwise. In
other words, determine if the second list is the first list shifted to the
right by 1.

### Examples

    simon_says([1, 2], [5, 1]) ➞ True
    
    simon_says([1, 2], [5, 5]) ➞ False
    
    simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
    
    simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False

### Notes

  * Both input lists will be of the same length, and will have a minimum length of 2.
  * The values of the `0`-indexed element in the second list and the `n-1`th indexed element in the first list do not matter.

"""

def simon_says(lst1, lst2):
  cnt = 1
  boole = True
  for x in lst1:
    if cnt == len(lst1):
      break
    elif x == lst2[cnt]:
      cnt += 1
    else:
      boole = False
  return(boole)

