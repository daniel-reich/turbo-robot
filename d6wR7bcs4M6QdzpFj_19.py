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
    lst *= n
    return lst
  
​
def add(lst, x):
    lst += [x]
    return lst
  
​
def remove(lst, i, j):
    for k in range(i, j + 1):
        lst.remove(lst[i])
    return lst
        
​
def concat(lst, lst2):
    lst += lst2
    return lst
