"""


Write a function that replaces each integer with the next largest in the list.

### Examples

    replace_next_largest([5, 7, 3, 2, 8]) ➞ [7, 8, 5, 3, -1]
    
    replace_next_largest([2, 3, 4, 5]) ➞ [3, 4, 5, -1]
    
    replace_next_largest([1, 0, -1, 8, -72]) ➞ [8, 1, 0, -1, -1]

### Notes

  * Replace the maximum with **-1**.
  * Elements in the list will be unique.
  * You don't have to swap the elements.

"""

def replace_next_largest(lst):
    a = sorted([(i[1], i[0]) for i in enumerate(lst)]) 
    a.append((-1, max(i[1] for i in a)+1))
    b = [(a[i+1][0], a[i][1]) for i in range(len(a)-1)] 
    c = sorted((i[1], i[0]) for i in b)
    return [i[1] for i in c]

