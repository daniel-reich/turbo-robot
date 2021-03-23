"""


Write **four** functions that **directly mutate** a list:

  1.  **repeat(lst, n)** : Repeat `lst` **n** times.
  2.  **add(lst, x)** : Adds `x` to the **end** of the `lst`.
  3.  **remove(lst, m, n)** : Removes all elements between indices `m` and `n` **inclusive** in `lst`.
  4.  **concat(lst, x)** : concatenates `lst` with `x` (another list).

### Examples

    lst = [1, 2, 3, 4]
    
    repeat(lst, 3) ➞ [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4] 
    
    add(lst, 1) ➞ [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1]
    
    remove(lst, 1, 12) ➞ [1]
    
    concat(lst, [3, 4]) ➞ [1, 3, 4]

### Notes

Your functions should mutate the list directly, not make a copy.

"""

def repeat(lst, n):
    lst_copy = lst[:]
    t = 0
    while t < n-1:
      for a in lst_copy:
        lst.append(a)
      t += 1
    return lst
​
def add(lst, x):
  lst.append(x)
  return lst
​
def remove(lst, i, j):
  range_x = lst[i-1:j]
  for i in range_x:
    lst.remove(i)
  return lst
  
def concat(lst, lst2):
  for f in lst2:
    lst.append(f)
  return lst

