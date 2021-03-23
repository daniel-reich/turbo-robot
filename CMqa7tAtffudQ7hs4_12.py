"""


Given a shuffled list `l`, return a sequence of _transpositions_ which sorts
the list (as in `sorted(l)`). A transposition is a pair of indices `(i, j)`
representing that `l[i]` and `l[j]` be swapped. Specifically, the output is a
list of transpositions to be applied. Transpositions are applied as in:

    def apply_transpositions(l, swaps):
      for i, j in swaps:
      l[i], l[j] = l[j], l[i]
    return l

### Examples

    sorting_steps([5, -5]) ➞ [(0, 1)]
    # Swap first and second elements.
    
    sorting_steps([4, 3, 2, 1]) ➞ [(0, 3), (1, 2)] or even [(0, 1), (1, 2), (2, 3), (0, 1), (1, 2), (0, 1)]
    
    sorting_steps([6, 6]) ➞ []

### Notes

Output is not unique! A given list may be sorted with varying numbers of
transpositions stemming from various sorting techniques. You need only produce
output which works. (This gives the problem algorithimic freedom!)

"""

def sorting_steps(lst, start=0, end=None):
  if end is None: 
    end = len(lst)
    lst =lst[:]
  if end - start < 2: return []
  swaps = []
  pivot = lst[start]
  pIdx = start
  for i in range(start + 1, end):
    if lst[i] < pivot:
      # swap i, pIdx
      swaps.append( (i, pIdx) )
      lst[i], lst[pIdx] = lst[pIdx], lst[i]
      # swap swap i, pIdx + 1
      swaps.append((i, pIdx + 1))
      lst[i], lst[pIdx + 1] = lst[pIdx + 1], lst[i]
      pIdx += 1
  return swaps + sorting_steps(lst, start, pIdx) + sorting_steps(lst, pIdx + 1, end)

