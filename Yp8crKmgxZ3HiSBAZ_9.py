"""


Create a function that takes in a nested list and an element and returns the
frequency of that element by nested level.

### Examples

    freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1)
    ➞ [[0, 1], [1, 2], [2, 3]]
    # The list has one 1 at level 0, 2 1's at level 1, and 3 1's at level 2.
    
    freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5)
    ➞ [[0, 3], [1, 4], [2, 0]]
    
    freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2)
    ➞ [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]

### Notes

  * Start the default nesting (a list with no nesting) at 0.
  * Output the nested levels in order (e.g. 0 first, then 1, then 2, etc).
  * Output 0 for the frequency if that particular level has no instances of that element (see example #2).

"""

def freq_count(lst, el):
  def find_nesting(lst, n=0):
    items = []
    lists = []
​
    for item in lst:
      if isinstance(item, list) == True:
        for i in item:
          lists.append(i)
      else:
        items.append([n, item])
    
    if len(items) == 0:
      items.append([n, 'N'])
    if len(lists) == 0:
      return items
    else:
      return items + find_nesting(lists, n+1)
  
  nesting = find_nesting(lst)
  nests = {}
​
  for nest in nesting:
    nst = nest[0]
    item = nest[1]
​
    if nst not in nests.keys():
      nests[nst] = [item]
    else:
      nests[nst].append(item)
  
  frequency = []
  
  for freq in nests.keys():
    lst = nests[freq]
    count = lst.count(el)
    
    frequency.append([freq,count])
  
  return frequency

