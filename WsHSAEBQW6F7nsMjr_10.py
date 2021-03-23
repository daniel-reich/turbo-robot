"""


Given a list of integers, replace every number with the _mean_ of all numbers.

### Examples

    flatten_the_curve([1, 2, 3, 4, 5]) ➞ [3, 3, 3, 3, 3]
    
    flatten_the_curve([0, 0, 0, 2, 7, 3]) ➞ [2, 2, 2, 2, 2, 2]
    
    flatten_the_curve([4]) ➞ [4]
    
    flatten_the_curve([]) ➞ []

### Notes

  * Round averages to **1 decimal point**.
  * Return an empty list if given an empty list (see example #4).

"""

def flatten_the_curve(lst):
  if lst==[]:
    return []
  return [round(sum(lst)/len(lst),1) for i in range(0,len(lst))]

