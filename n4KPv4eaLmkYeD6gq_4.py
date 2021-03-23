"""


In mathematics, _interval_ is the difference between the largest number and
the smallest number in a list.

To illustrate:

    A = (3, 5, 7, 23, 11, 42, 80)
    
    Interval of A = 80 - 3 = 77

Create a function that takes a list and returns `":)"` if the interval of the
list is equal to any other element; otherwise return `":("`.

### Examples

    face_interval([1, 2, 5, 8, 3, 9]) ➞ ":)"
    # List interval is equal to one of the other elements.
    
    face_interval([5, 2, 8, 3, 11]) ➞ ":("
    # List interval is not among the other elements.
    
    face_interval("bruh") ➞ ":/"
    # "bruh" is not a list. It's string.

### Notes

  * Lists won't contain any duplicate numbers.
  * If you're not given a list, return `":/"`

"""

def face_interval(num):
  lst = num
  if type(lst) == list:
    interv = max(lst) - min(lst)
    return ":)" if interv in lst else ":("
  else:
    return ":/"

