"""


Write a function that takes two lists (`lst1` and `lst2`) and an int `n`, and
returns `True` if the second list equals the first list shifted by `n`
positions. Otherwise, return `False`.

### Examples

    circular_shift([1, 2, 3, 4], [3, 4, 1, 2], 2) ➞ True
    
    circular_shift([1, 1], [1, 1], 6) ➞ True
    
    circular_shift([0, 1, 2, 3, 4, 5], [3, 4, 5, 2, 1, 0], 3) ➞ False

### Notes

  * The two lists will have the same length.
  * `n` can be a negative value.

"""

def circular_shift(lst1, lst2, n):
  if n==0: return lst1==lst2
  elif n>0:
    return lst1[0:len(lst1)-n]==lst2[n:]
  else:
    n=n*-1
    return lst2[0:len(lst2)-n]==lst1[n:]

