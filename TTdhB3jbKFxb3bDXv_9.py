"""


Create two functions: a **left-shift function** and a **right-shift
function**. Each function will take in a list and a single parameter: the
number of shifts.

    [1, 2, 3, 4, 5]
    
    [2, 3, 4, 5, 1]  # left shift of 1
    [5, 1, 2, 3, 4]  # left shift of 4
    
    [5, 1, 2, 3, 4]  # right shift of 1
    [3, 4, 5, 1, 2]  # right shift of 3

### Examples

    left_shift([1, 2, 3, 4], 1) ➞ [2, 3, 4, 1]
    
    right_shift([1, 2, 3, 4], 1) ➞ [4, 1, 2, 3]
    
    left_shift([1, 2, 3, 4, 5], 3) ➞ [4, 5, 1, 2, 3]
    
    left_shift([1, 2, 3, 4, 5], 5) ➞ [1, 2, 3, 4, 5]
    # You have fully shifted the list, you end up back where you began.
    
    left_shift([1, 2, 3, 4, 5], 6) ➞ [2, 3, 4, 5, 1]
    # You should be able to take in numbers greater than the length.
    # Think of the length of the list as a modulo.

### Notes

  * `n` might be higher than the number of values in the list.
  * `n` will never be negative.

"""

def left_shift(lst, n):
  if n%len(lst)==0:
    return lst
  elif n<len(lst):
    return lst[n:len(lst)]+lst[0:n]
  else:
    return lst[n%len(lst):len(lst)]+lst[0:n%len(lst)]
​
def right_shift(lst, n):
  if n%len(lst)==0:
    return lst
  elif n<len(lst):
    return lst[-n:]+lst[0:len(lst)-n]
  else: 
    return lst[-n%len(lst):]+lst[0:len(lst)-n%len(lst)]

