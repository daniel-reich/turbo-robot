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
  
  if n >= 0:
    for i in range(n):
      temp = lst1[0]
      lst1.pop(0)
      lst1.append(temp)
  else:
    for i in range(n,0,1):
      temp = lst1[-1]
      lst1.pop(-1)
      lst1.insert(0, temp)
​
  return lst1 == lst2

