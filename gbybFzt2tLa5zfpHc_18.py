"""


Write a function that returns all sets of three elements that sum to 0.

### Examples

    three_sum([0, 1, -1, -1, 2]) ➞ [[0, 1, -1], [-1, -1, 2]]
    
    three_sum([0, 0, 0, 5, -5]) ➞ [[0, 0, 0], [0, 5, -5]]
    
    three_sum([1, 2, 3]) ➞ []
    
    three_sum([1]) ➞ []

### Notes

  * The original list **may contain duplicate numbers**.
  * Each three-element sublist in your output should be **distinct**.
  * Sublists should be ordered by the first element of the sublist.
  * Sublists themselves should be ordered the same as the original list.
  * Return an empty list if no three elements sum to zero.
  * Return an empty list if there are fewer than three elements.

"""

def three_sum(lst):
  sols = []
  for ka, va in enumerate(lst[:-2]):
    for kb, vb in enumerate(lst[ka+1:-1]):
      for kc, vc in enumerate(lst[ka+1+kb+1:]):
        if sum([va, vb, vc]) == 0:
          if [va, vb, vc] not in sols:
            sols.append([va, vb, vc])
  return sols

