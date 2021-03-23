"""


Write a function that transforms an array into an array of its differences
repeatedly until there exists only one element left. A difference is `A[n+1] -
A[n]`.

To illustrate:

    [5, 1, 9, 3, 4, 0]
    
    [-4, 8, -6, 1, -4]
    # 1 - 5 = -4; 9 - 1 = 8; 3 - 9 = -6; etc.
    
    [12, -14, 7, -5]
    
    [-26, 21, -12]
    
    [47, -33]
    
    -80 

### Examples

    n_differences([5, 1, 9, 3, 4, 0]) ➞ -80
    
    n_differences([1, 1, 1, 1]) ➞ 0
    
    n_differences([5, 8, 8]) ➞ -3

### Notes

Each array will have at least two elements.

"""

def n_differences(lst):
  while len(lst) > 1:
    lst = descrease(lst)
  return lst[0]
​
def descrease(lst):
  return [lst[i + 1] - lst[i] for i in range(0,len(lst) - 1, 1)]

