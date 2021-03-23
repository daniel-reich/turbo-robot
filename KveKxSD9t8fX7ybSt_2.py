"""


A countdown sequence is a descending sequence of `k` integers from `k` down to
1 (e.g. 5, 4, 3, 2, 1). Write a function that returns a list `[x, y]` where
**x** is the number that represents how many of countdown sequences are in a
given list and **y** is a list of those sequences in order which they appear
in the list.

### Examples

    final_countdown([4, 8, 3, 2, 1, 2]) ➞ [1, [[3, 2, 1]]]
    # In this example we have 1 countdown sequence: 3, 2, 1
    
    final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]) ➞ [2, [[5, 4, 3, 2, 1], [3, 2, 1]]]
    # We have 2 countdown sequences:
    # 5, 4, 3, 2, 1 and 3, 2, 1
    
    final_countdown([4, 3, 2, 1, 3, 2, 1, 1]) ➞ [3, [[4, 3, 2, 1], [3, 2, 1], [1]]]
    # We have 3 countdown sequences:
    # 4, 3, 2, 1 ; 3, 2, 1 and 1
    
    final_countdown([1, 1, 2, 1]) ➞ [3, [[1], [1], [2, 1]]]
    
    final_countdown([]) ➞  [0, []]

### Notes

  * `[1]` is a valid countdown sequence.
  * All numbers will be greater than 0.

"""

def final_countdown(lst):
  res=[[lst[0]]] if lst else []
  for i in range(1,len(lst)):
    if lst[i-1]-lst[i]==1 and lst[i]!=0:res[-1]+=[lst[i]]
    else:res+=[[lst[i]]]
  res=[i for i in res if i[-1]==1]
  return [len(res),res]

