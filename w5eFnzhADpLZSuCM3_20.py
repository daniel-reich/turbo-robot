"""


Write a function that returns a list of elements `[number, multiplicity]`. The
`multiplicity` of a number refers to the number of times it occurs in the
list.

To illustrate:

    [5, 5, 1, 1, 5, 5, 3]
    [[5, 4], [1, 2], [3, 1]]
    
    # Since 5 appears 4 times, 1 appears twice, and 3 appearance once.

The final list should only include unique elements, and the elements should be
ordered by when they first appeared in the original list.

### Examples

    multiplicity([1, 1, 1, 2, 2, 3]) ➞ [[1, 3], [2, 2], [3, 1]]
    
    multiplicity([1, 1, 1, 1, 1]) ➞ [[1, 5]]
    
    multiplicity([1, 5, 4, 3, 2]) ➞ [[1, 1], [5, 1], [4, 1], [3, 1], [2, 1]]

### Notes

N/A

"""

def multiplicity(lst):
  l = []
  for x in lst:
    if all(x != y[0] for y in l):
      l.append([x, lst.count(x)])
  return l

