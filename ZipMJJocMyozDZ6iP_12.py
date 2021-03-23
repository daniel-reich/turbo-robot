"""


Create a function that groups a list of numbers based on a **size** parameter.
The **size** represents the maximum length of each sub-list.

    [1, 2, 3, 4, 5, 6], 3
    [[1, 3, 5], [2, 4, 6]]
    # Divide list into groups of size 3.
    
    [1, 2, 3, 4, 5, 6], 2
    [[1, 4], [2, 5], [3, 6]]
    # Divide list into groups of size 2.
    
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 4
    [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9]]
    # "Leftover" lists are okay.

### Examples

    group([1, 2, 3, 4], 2) ➞ [[1, 3], [2, 4]]
    
    group([1, 2, 3, 4, 5, 6, 7], 4) ➞ [[1, 3, 5, 7], [2, 4, 6]]
    
    group([1, 2, 3, 4, 5], 1) ➞ [[1], [2], [3], [4], [5]]
    
    group([1, 2, 3, 4, 5, 6], 4) ➞ [[1, 3, 5], [2, 4, 6]]

### Notes

  * The **size** parameter represents the maximum size for each sub-list (see ex.4). You should try to fill each sub-list evenly. In other words, ex.4 should be `[[1, 3, 5], [2, 4, 6]]`, not `[[1, 3, 5, 6], [2, 4]]`.
  * Keep the relative order of the numbers in each sub-list the same as the order in the original list.

"""

def group(lst, size):
  lstsize = int(len(lst) / size) + int(len(lst) % size != 0)
  r = [[] for i in range(lstsize)]
  isize = 0
  for i in lst:
    r[isize].append(i)
    isize = (isize + 1) % lstsize
  return r

