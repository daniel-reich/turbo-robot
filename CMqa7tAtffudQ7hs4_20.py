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

def sorting_steps(lst):
  def swap(lst, swaps = []):
    if lst == sorted(lst):
      return swaps
    else:
      s = []
      for n in range(1, len(lst)):
        pi = lst[n-1]
        ci = lst[n]
        if ci < pi:
          spi = ci
          sci = pi
          lst[n-1] = spi
          lst[n] = sci
          swaps.append(tuple([n-1, n]))
          break
      return swap(lst,swaps)
  swaps = swap(lst)
  return swaps

